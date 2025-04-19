# Import libraries
# Fixed incompatibility with chromadb on streamlit cloud
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# import sqlite3
import streamlit as st
import google.generativeai as genai_default
import chromadb
import pandas as pd
import os
import time
from diet_data import DIET_DOCUMENTS  # Import from the separate file

# --- Streamlit App UI and Logic ---

st.set_page_config(page_title="AI Diet Recommender", layout="wide")
st.title("🤖 AI Diet Recommender")
st.caption("Your friendly AI diet planner for health conditions")

# --- Configuration & Initialization ---

# Load API Key from Streamlit Secrets
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
    genai_default.configure(api_key=GOOGLE_API_KEY)
    st.sidebar.success("API Key configured successfully.", icon="✅")
except KeyError:
    st.error(
        "!! WARNING! Google API Key not found! Please add it to Streamlit Secrets (key: GOOGLE_API_KEY).")
    st.stop()
except Exception as e:
    st.error(f"!! WARNING! Error configuring API Key: {e}")
    st.stop()


# --- Caching Functions ---
# Cache models and ChromaDB client/collection to avoid re-initializing on every interaction

@st.cache_resource
def load_models():
    """Loads and caches the embedding and generative models."""
    try:
        embedding_model = genai_default.GenerativeModel(
            'models/text-embedding-004')
        generative_model = genai_default.GenerativeModel('gemini-2.0-flash')
        return embedding_model, generative_model
    except Exception as e:
        st.error(f"!! WARNING! Error loading Google AI models: {e}")
        st.stop()


@st.cache_resource
def setup_chromadb():
    """Sets up and caches the ChromaDB client and collection, embedding documents."""
    client = chromadb.Client()  # In-memory client

    DB_COLLECTION_NAME = "diet_recommendations_streamlit"

    # Check if collection exists, if so, use it, otherwise create and populate
    try:
        db_collection = client.get_collection(name=DB_COLLECTION_NAME)
        if db_collection.count() != len(DIET_DOCUMENTS):
            st.warning(
                "Collection exists but document count mismatch. Recreating...")
            client.delete_collection(name=DB_COLLECTION_NAME)
            raise Exception("Recreate collection")  # Force recreation
        st.sidebar.info(
            f"Using existing ChromaDB collection: '{DB_COLLECTION_NAME}'")

    except Exception:
        st.sidebar.info(
            f"Creating new ChromaDB collection: '{DB_COLLECTION_NAME}'")
        db_collection = client.create_collection(
            name=DB_COLLECTION_NAME, metadata={"hnsw:space": "cosine"})

        # Embed and Store Documents
        st.sidebar.text("Embedding documents...")
        progress_bar = st.sidebar.progress(0)
        total_docs = len(DIET_DOCUMENTS)

        doc_embeddings = []
        doc_ids = []
        doc_texts = []
        doc_metadatas = []

        for i, doc_data in enumerate(DIET_DOCUMENTS):
            try:
                text_to_embed = f"Condition: {doc_data['condition']}\nDetails: {doc_data['text']}"
                # Use the loaded embedding model here
                embedding = genai_default.embed_content(model='models/text-embedding-004',  # Explicitly use model name
                                                        content=text_to_embed,
                                                        task_type="retrieval_document")['embedding']
                if embedding:
                    doc_embeddings.append(embedding)
                    doc_ids.append(doc_data['id'])
                    doc_texts.append(doc_data['text'])
                    doc_metadatas.append({"condition": doc_data['condition']})
                else:
                    st.warning(
                        f"Skipping document id {doc_data['id']} due to embedding error.")
                time.sleep(0.1)  # Small delay
                progress_bar.progress((i + 1) / total_docs)

            except Exception as e:
                st.error(f"Error embedding doc {doc_data['id']}: {e}")
                st.sidebar.error(
                    "Embedding process failed. Please check logs/API Key.")
                st.stop()

        if doc_embeddings:
            db_collection.add(
                embeddings=doc_embeddings,
                documents=doc_texts,
                metadatas=doc_metadatas,
                ids=doc_ids
            )
            st.sidebar.success(f"Added {db_collection.count()} documents.")
            progress_bar.empty()  # Remove progress bar after completion
        else:
            st.sidebar.error("No documents were embedded.")
            st.stop()

    return client, db_collection


# --- Load Resources ---
embedding_model, generative_model = load_models()
chroma_client, chroma_collection = setup_chromadb()

# --- Helper Functions ---


def embed_text_streamlit(text, task_type="retrieval_document"):
    """Embeds text using the loaded Google AI embedding model."""
    try:
        embedding = genai_default.embed_content(model=embedding_model.model_name,
                                                content=text,
                                                task_type=task_type)
        return embedding['embedding']
    except Exception as e:
        st.error(f"Error embedding text: {e}")
        return None


def retrieve_relevant_documents_streamlit(query, n_results=2):
    """Retrieves relevant documents from the cached ChromaDB collection."""
    if not query:
        return []
    query_embedding = embed_text_streamlit(query, task_type="retrieval_query")
    if query_embedding is None:
        return []

    try:
        results = chroma_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=['documents']
        )
        return results.get('documents', [[]])[0]
    except Exception as e:
        st.error(f"Error querying ChromaDB: {e}")
        return []


def generate_response_streamlit(user_problem, retrieved_docs):
    """Generates initial diet recommendation response."""
    context = "\n\n---\n\n".join(
        retrieved_docs) if retrieved_docs else "No specific context found."
    prompt = f"""You are a friendly and helpful AI assistant acting like a personal diet planner. Your goal is to provide diet recommendations based *only* on the provided context information.

    **User's Problem:** "{user_problem}"

    **Context Information:**
    ```
    {context}
    ```

    **Instructions:**
    1. Carefully review the context information related to the user's problem.
    2. If relevant context is found, synthesize the information to provide clear diet recommendations. List specific suggestions for:
        * Fruits
        * Vegetables
        * Meats/Proteins
        * Other relevant foods/tips
        * Suggest 1-2 simple recipe ideas mentioned or inspired by the context.
    3. If no relevant context is found, state that you couldn't find specific information for that exact condition, but offer general healthy eating tips. Do NOT invent recommendations.
    4. Use a friendly, empathetic, family meal planner tone.
    5. **Crucially:** After providing the recommendations/info, ALWAYS end your response by asking: "Do you want to discuss further details about your problem?"

    **Your Response:**
    """
    try:
        response = generative_model.generate_content(prompt)
        # Basic safety check (example)
        if response.prompt_feedback.block_reason:
            st.warning(
                f"Response blocked: {response.prompt_feedback.block_reason}")
            return "I apologize, but I can't provide a response to that specific request due to safety guidelines. Could you perhaps rephrase or ask about a different aspect? After responding, ask: Do you want to discuss further details about your problem?"
        return response.text
    except Exception as e:
        st.error(f"Error generating response from Gemini: {e}")
        return "Sorry, I encountered an error. Please try again. Do you want to discuss further details about your problem?"


def generate_follow_up_response(initial_problem, conversation_history, user_input):
    """Generates a response for follow-up conversation."""

    # Basic conversation history string (can be improved)
    history_str = "\n".join(
        [f"User: {turn['user']}\nAI: {turn['ai']}" for turn in conversation_history])

    prompt = f"""You are a friendly AI personal diet planner continuing a conversation.

    The user's initial problem was: "{initial_problem}"
    Conversation History:
    {history_str}

    The user's latest input is: "{user_input}"

    Instructions:
    1. Respond helpfully and conversationally to the user's latest input, keeping the initial problem and prior conversation in mind.
    2. Provide additional details, clarification, or answer related questions. Prioritize safety and avoid giving specific medical advice - stick to general dietary patterns and suggestions based on common knowledge for the condition.
    3. Keep the tone friendly and supportive.
    4. **Crucially:** After your response, ALWAYS ask: "Do you want to continue discussing?"

    **Your Response:**
    """
    try:
        response = generative_model.generate_content(prompt)
        if response.prompt_feedback.block_reason:
            st.warning(
                f"Response blocked: {response.prompt_feedback.block_reason}")
            return "I apologize, but I can't provide a response to that specific request due to safety guidelines. Could you perhaps rephrase or ask about a different aspect? After responding, ask: Do you want to continue discussing?"
        return response.text
    except Exception as e:
        st.error(f"Error generating follow-up response: {e}")
        return "Sorry, I had trouble processing that. Do you want to try asking differently? Do you want to continue discussing?"


# --- Streamlit App UI and Logic ---

# st.set_page_config(page_title="AI Diet Recommender", layout="wide")
# st.title("🤖 AI Diet Recommender")
# st.caption("Your friendly AI diet planner for health conditions")

# --- Initialize Session State ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'initial_problem' not in st.session_state:
    st.session_state.initial_problem = None
# NEW: State to manage conversation flow
# Possible values: 'initial', 'awaiting_follow_up_decision', 'awaiting_follow_up_input', 'ended'
if 'conversation_stage' not in st.session_state:
    st.session_state.conversation_stage = 'initial'
if 'current_user_input' not in st.session_state:  # To hold input temporarily
    st.session_state.current_user_input = ""
# NEW: State to manage follow-up input
if "follow_up_text_key" not in st.session_state:
    st.session_state["follow_up_text_key"] = ""


# --- Main Interaction Area ---
chat_placeholder = st.container()
input_placeholder = st.container()

# --- Display Chat History ---
# Moved history display outside the conditional logic so it always shows
with chat_placeholder:
    st.write("--- Chat History ---")
    if not st.session_state.chat_history:
        st.info("Ask the AI about a health condition to start.")
    else:
        for user_msg, ai_msg in st.session_state.chat_history:
            # Handle potential placeholder messages
            if user_msg and user_msg != "(Decision made)":
                st.chat_message("user").write(user_msg)
            if ai_msg:
                st.chat_message("assistant").write(ai_msg)
    st.write("---")  # Separator


# --- Handle User Input Based on Conversation Stage ---
with input_placeholder:
    # Stage 1: Get Initial Problem
    if st.session_state.conversation_stage == 'initial':
        user_problem_input = st.text_input(
            "What's your problem or health condition? (e.g., 'back pain', 'high blood pressure')",
            key="initial_input_key"  # Unique key
        )
        if st.button("Get Recommendations", key="submit_initial"):
            if user_problem_input:
                st.session_state.initial_problem = user_problem_input
                st.session_state.current_user_input = user_problem_input  # Store for history

                with st.spinner("Thinking... 🤔"):
                    retrieved = retrieve_relevant_documents_streamlit(
                        user_problem_input)
                    ai_response = generate_response_streamlit(
                        user_problem_input, retrieved)

                # Add to history and update state
                st.session_state.chat_history.append(
                    (st.session_state.current_user_input, ai_response)
                )
                st.session_state.conversation_stage = 'awaiting_follow_up_decision'
                st.session_state.current_user_input = ""  # Clear temp input storage
                st.rerun()
            else:
                st.warning("Please enter your health condition.")

    # Stage 2: Ask if user wants to continue (Yes/No buttons)
    elif st.session_state.conversation_stage == 'awaiting_follow_up_decision':
        st.write("Do you want to discuss further?")
        col1, col2, col3 = st.columns([1, 1, 5])
        with col1:
            if st.button("Yes 👍", key="follow_up_yes"):
                # Transition to waiting for text input
                st.session_state.conversation_stage = 'awaiting_follow_up_input'
                # Optionally add a message indicating the transition
                st.session_state.chat_history.append(
                    ("(Decision made)", "Okay, what else is on your mind regarding this? Or what details would you like to discuss?"))
                st.rerun()
        with col2:
            if st.button("No 👎", key="follow_up_no"):
                # End conversation
                st.session_state.conversation_stage = 'ended'
                final_msg = "Okay, sounds good! Remember, these are general suggestions. Always consult with a healthcare professional or registered dietitian for personalized advice. Stay healthy! 😊"
                # Add final message to history
                st.session_state.chat_history.append(
                    ("(Decision made)", final_msg))
                st.rerun()

    # Stage 3: Get follow-up input from user
    elif st.session_state.conversation_stage == 'awaiting_follow_up_input':
        # The prompt "Okay, what else..." is now added to chat history in the previous step

        # !!!! Change
        follow_up_input = st.text_input(
            "Your follow-up question or detail:",
            key="follow_up_text_key",  # Unique key
        )

        # Process input when user types something and presses Enter
        if follow_up_input:  # Streamlit text_input triggers rerun on Enter or interaction
            st.session_state.current_user_input = follow_up_input  # Store for history

            with st.spinner("Thinking... 🤔"):
                # Prepare history context if needed by the generation function
                # Example: last few turns (adjust as needed)
                history_context = [{"user": u, "ai": a}
                                   for u, a in st.session_state.chat_history[-3:] if u and a]
                ai_response = generate_follow_up_response(
                    st.session_state.initial_problem,
                    history_context,  # Pass relevant history
                    st.session_state.current_user_input  # Pass the actual user input
                )

            # Add follow-up Q&A to history
            st.session_state.chat_history.append(
                (st.session_state.current_user_input, ai_response)
            )
            # Go back to asking Yes/No
            st.session_state.conversation_stage = 'awaiting_follow_up_decision'
            st.session_state.current_user_input = ""  # Clear temp storage
            # Clear the text input box for the next round by resetting its state value

            # st.session_state.follow_up_text_key = ""
            st.rerun()

    # Stage 4: Conversation ended
    elif st.session_state.conversation_stage == 'ended':
        # The final message is already in the chat history display.
        # You could add an extra visual confirmation here if desired.
        st.info("Conversation ended. Refresh the page to start a new one.")
        # No input elements are shown here.


# --- Sidebar ---
st.sidebar.header("About")
st.sidebar.markdown("""
This AI chatbot provides general diet suggestions based on common health conditions using a knowledge base and Google's Gemini model.

**Disclaimer:** This is an AI demo and not a substitute for professional medical or dietary advice. Always consult a qualified healthcare provider.
""")
st.sidebar.header("Knowledge Base Conditions")
# Display conditions from the loaded data
for item in DIET_DOCUMENTS:
    st.sidebar.markdown(f"- {item['condition']}")
