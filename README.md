# AI Condition Based Diet Recommendation Chatbot 🤖🥗

## Google Gen AI Intensive Course Capstone 2025Q1

This capstone project is a part of 5-day Gen AI Intensive Course with Google and Kaggle held in March 2025. The course was designed to help participants learn about the latest advancements in AI and how to apply them in real-world scenarios.

**Problem defenition**
Based on personal experience. Health education in my country is extremely limited to nonexistent. People are often discharged from hospitals with medication but little to no guidance on how diet and lifestyle can support recovery. There is a lack of accessible tools that guide people in using food as a complementary therapy. This gap inspired this project to develop of an AI chatbot that recommends personalized dietary strategies based on current health conditions, aiming to support healing, improve outcomes, and minimize excessive and unnecessary use of generic drugs.

The chatbot is designed to provide dietary suggestions based on specific health conditions, such as high blood pressure or back pain. It retrieves relevant information from a knowledge base and generates responses using the Gemini model, ensuring that the recommendations are tailored to the user's needs.

It utilizes Google's Gemini model for conversational AI and response generation, combined with a Retrieval-Augmented Generation (RAG) approach. A basic knowledge base of dietary information is embedded and stored in a ChromaDB vector database for efficient retrieval.

**Disclaimer:** This tool provides general information based on its knowledge base and AI generation. **It is NOT a substitute for professional medical or dietary advice.** Always consult with a qualified healthcare provider or registered dietitian for personalized recommendations specific to your health situation.

## Features

- **Condition-Based Recommendations:** Users can state their health issue (e.g., "back pain", "high blood pressure").
- **RAG Implementation:** Retrieves relevant dietary information from a vector store (ChromaDB) before generating a response.
- **Model:** Uses Google's `gemini-2.0-flash` for understanding queries and generating human-like responses.
- **Specific Suggestions:** Aims to provide lists of recommended fruits, vegetables, proteins, and simple recipe ideas based on retrieved context.
- **Conversational Flow:** Engages in a basic follow-up conversation if the user wishes to discuss further.
- **Persona:** Instructed to act like a helpful "personal diet planner".
- **Kaggle Notebook:** Includes a Jupyter notebook (`diet_chatbot_rag_build_v25.ipynb`) designed to run on Kaggle, demonstrating the core logic.
- **Streamlit App:** Includes a Python script (`diet_chatbot_app.py`) to deploy the chatbot as an interactive web application using Streamlit.

## How it Works

1. **Knowledge Base:** Sample dietary information for different conditions is stored in `diet_data.py`.
2. **Embedding:** This knowledge base is processed, and each document is converted into a numerical vector (embedding) using Google's `text-embedding-004` model.
3. **Vector Store:** These embeddings and the corresponding text documents are stored in a ChromaDB collection (in-memory for simplicity).
4. **User Query:** When the user provides their health condition, their query is also embedded.
5. **Retrieval:** ChromaDB is queried to find the documents in the knowledge base whose embeddings are most similar (semantically) to the user's query embedding.
6. **Generation:** The user's query and the retrieved documents (context) are fed into the Gemini (`gemini-2.0-flash`) model with a specific prompt instructing it to act as a meal planner and generate recommendations based _only_ on the provided context.
7. **Interaction:** The Streamlit app manages the chat interface, state (like whether a recommendation has been given), and the follow-up conversation loop.

## Setup and Running

**Prerequisites:**

- Python 3.8+
- Google AI API Key

**1. Get API Key:**

- Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- Head to .streamlit/secrets.toml.example and rename it to secrets.toml.
- Add your API key to the secrets.toml file (replace "YOUR_GOOGLE_API_KEY" with your actual API key):

  ```bash
  GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
  ```

- If deployed on Streamlit Cloud, add the secret under App Settings > Secrets.

**2. Clone Repository (Optional):**

```bash
git clone <repository-url>
cd <repository-directory>
```

**3. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**4. Set up API Key:**

- For Streamlit (Recommended): Use Streamlit's secrets management. Create a file .streamlit/secrets.toml in your project directory with the following content:

```bash
GOOGLE_API_KEY = "YOUR_API_KEY"
```

- For Local/Notebook (Alternative): Create a .env file in the root directory:

```bash
GOOGLE_API_KEY=YOUR_API_KEY
```

The notebook and script can load this using python-dotenv if secrets aren't available (primarily for local testing).

- For Kaggle Notebook: Use Kaggle's "Secrets" feature (Add-ons -> Secrets). Add a secret named GOOGLE_API_KEY with your API key as the value.

**5. Running:**

- Kaggle Notebook:

  - Upload AI_Dietitian_Kaggle.ipynb and diet_data.py (or copy the data into the notebook).
  - Ensure the GOOGLE_API_KEY secret is set.
  - Run the cells sequentially.

- Streamlit App:

  - Make sure diet_chatbot_app.py, diet_data.py, and requirements.txt are in the same directory.
  - Ensure your API key is configured (preferably via `.streamlit/secrets.toml`).
  - Run the app from your terminal:

    ```bash
    streamlit run diet_chatbot_app.py
    ```

  - Access the app in your web browser through the URL provided by Streamlit (usually <http://localhost:8501>).

## How to Use the App

1. Open the web interface.
2. Type your health condition in the input box (e.g., "I have high blood pressure").
3. Press Enter or click the "Get Recommendations" button.
4. The chatbot will respond with dietary recommendations based on the condition you provided.
5. At the end of the response, the chatbot will ask if you want to continue the conversation.
6. If you want to continue, click "yes" or "no" button.
7. If you click "yes", the chatbot will ask for a follow-up question or provide additional suggestions.
8. If you click "no", the chatbot will end the conversation.

Get responses from the chatbot in real-time!

## Example Usage

1. **User Input:** "I have high blood pressure."
2. **Chatbot Response:** "For high blood pressure, consider incorporating more fruits like bananas and vegetables like spinach into your diet. Avoid excessive salt and processed foods."
3. **Follow-up:** "Can you suggest a simple recipe?"
4. **Chatbot Response:** "How about a spinach and banana smoothie? Just blend spinach, a banana, and some almond milk. It's refreshing and good for you!"
5. **User Input:** "What about back pain?"
6. **Chatbot Response:** "For back pain, consider foods rich in omega-3 fatty acids like salmon and walnuts. Also, stay hydrated and maintain a balanced diet."
7. **Follow-up:** "Can you suggest a simple recipe?"
8. **Chatbot Response:** "You can try a salmon salad with mixed greens, walnuts, and a light vinaigrette. It's nutritious and easy to prepare!"

## Files

- diet_chatbot_rag_build.ipynb: Jupyter Notebook for development and Kaggle execution. (Check out the [Kaggle](https://www.kaggle.com/code/peterjordanson10/condition-based-diet-recommender-rag) version of the notebook)
- diet_chatbot_app_v2.py: Python script for the Streamlit web application.
- diet_data.py: Contains the sample knowledge base documents.
- requirements.txt: Lists Python package dependencies.
- README.md: This file.
- .streamlit/secrets.toml (Create this if you want to deploy the app using streamlit): For storing API keys securely for Streamlit.
- .env (Optional, create this if you want to run the app locally): Alternative for local API key storage.
- Note that there may be additional files created by Streamlit during runtime, such as .streamlit/config.toml, which are not included in the repository. These files are automatically generated and **should not be modified**.
- Some other files might be added in the future for additional features, fixes, or improvements.

## Limitations & Future Improvements

- Limited Knowledge Base: The sample data in diet_data.py is very basic. A real application needs a comprehensive, medically validated database.
- No Real-time Data: Doesn't access external, up-to-the-minute medical information.
- Basic RAG: Retrieval is based on simple similarity. More advanced techniques could improve relevance.
- No User Profiles: Doesn't store user history, allergies, or preferences across sessions.
- Safety: While basic prompts guide the AI, more robust safety layers and content filtering would be needed for a production app.
- Error Handling: Basic error handling is included, but could be more comprehensive.

---

This setup gives you a functional prototype. Remember to handle that API key securely, especially when deploying.
Play around and tinker with your own version of this RAG app by forking this repo. Let me know if you have any questions or suggestions for improvements!

- **Contributions:** Feel free to fork the repo and submit pull requests for improvements or additional features.
- **Feedback:** Open an issue for any bugs or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- [LinkedIn](https://www.linkedin.com/in/robert-modalo-78b97580)
- [Medium](https://medium.com/@robertmodalo2)
- [GitHub](https://github.com/robertmodalocodes)
