# diet_data.py

# Simple knowledge base mapping conditions to dietary advice
# In a real app, this would be much more extensive and validated by professionals.
DIET_DOCUMENTS = [
    {
        "id": "doc1",
        "condition": "Back Pain / Inflammation",
        "text": """
        **Diet Recommendations for Back Pain & Inflammation:**

        *Focus on anti-inflammatory foods.*

        **Fruits:** Berries (blueberries, strawberries, raspberries), cherries, pineapple, oranges, apples. These are rich in antioxidants and vitamins.
        **Vegetables:** Leafy greens (spinach, kale, Swiss chard), broccoli, bell peppers, carrots, sweet potatoes. Packed with vitamins, minerals, and fiber.
        **Meats/Proteins:** Fatty fish (salmon, mackerel, sardines - high in Omega-3s), lean poultry (chicken breast, turkey), legumes (beans, lentils), tofu, nuts, and seeds (walnuts, flaxseeds, chia seeds). Limit red meat and processed meats.
        **Other:** Olive oil, turmeric, ginger, green tea. Stay well-hydrated with water. Avoid sugary drinks, refined carbohydrates (white bread, pasta), fried foods, and excessive saturated fats.

        **Simple Recipe Idea: Salmon with Roasted Veggies**
        *   Toss chopped sweet potatoes, broccoli florets, and red bell pepper strips with olive oil, salt, pepper, and a pinch of turmeric. Roast at 400°F (200°C) for 20-25 minutes.
        *   Season salmon fillets with salt, pepper, and lemon juice. Add to the baking sheet with veggies for the last 12-15 minutes of cooking, or until salmon is cooked through.
        *   Serve immediately.
        """
    },
    {
        "id": "doc2",
        "condition": "High Blood Pressure (Hypertension)",
        "text": """
        **Diet Recommendations for High Blood Pressure (Hypertension):**

        *Focus on the DASH (Dietary Approaches to Stop Hypertension) diet principles. Emphasize low sodium.*

        **Fruits:** Bananas (potassium), berries, apples, oranges, peaches, melons. Aim for 4-5 servings daily.
        **Vegetables:** Leafy greens, broccoli, carrots, tomatoes, potatoes (especially sweet potatoes). Aim for 4-5 servings daily.
        **Meats/Proteins:** Lean meats (skinless poultry, fish), beans, lentils, nuts, seeds. Limit red meat. Aim for 6 or fewer ounces per day.
        **Grains:** Whole grains (oatmeal, brown rice, whole wheat bread/pasta). Aim for 6-8 servings daily.
        **Dairy:** Low-fat or fat-free milk, yogurt, cheese. Aim for 2-3 servings daily.
        **Other:** Limit sodium intake significantly (aim for under 1500mg/day if possible, definitely under 2300mg). Reduce added sugars, saturated fats, and trans fats. Use herbs and spices for flavor instead of salt. Stay hydrated.

        **Simple Recipe Idea: Chicken and Veggie Stir-fry with Brown Rice**
        *   Cook brown rice according to package directions.
        *   Stir-fry sliced chicken breast in a little sesame or olive oil until cooked. Remove from wok/pan.
        *   Add chopped vegetables (broccoli, bell peppers, carrots, snow peas) and stir-fry until tender-crisp.
        *   Add chicken back to the pan. Toss with a low-sodium soy sauce (or coconut aminos), ginger, and garlic.
        *   Serve over brown rice.
        """
    },
    {
        "id": "doc3",
        "condition": "Type 2 Diabetes Management",
        "text": """
        **Diet Recommendations for Type 2 Diabetes Management:**

        *Focus on controlling blood sugar levels through balanced meals, portion control, and carbohydrate awareness.*

        **Fruits:** Berries, apples, pears, oranges, melon. Choose whole fruits over juices. Be mindful of portion sizes due to natural sugars.
        **Vegetables:** Non-starchy vegetables are excellent (leafy greens, broccoli, cauliflower, bell peppers, green beans, zucchini). Include starchy vegetables (potatoes, corn, peas) in moderation and count them as carbs.
        **Meats/Proteins:** Lean protein sources like fish, skinless poultry, beans, lentils, tofu, eggs, nuts in moderation. Helps with satiety and doesn't spike blood sugar significantly.
        **Grains:** Whole grains (quinoa, brown rice, oats, whole wheat bread - check labels for fiber content). Portion control is key for carbohydrate counting.
        **Dairy:** Low-fat or non-fat milk, yogurt (plain), cheese in moderation.
        **Other:** Healthy fats (avocado, olive oil, nuts, seeds). Limit sugary drinks, sweets, processed foods, white bread/rice/pasta, and trans fats. Focus on fiber-rich foods. Consistent meal timing can help manage blood sugar. Stay hydrated with water.

        **Simple Recipe Idea: Lentil Soup**
        *   Sauté chopped onions, carrots, and celery in a pot with a little olive oil.
        *   Add vegetable broth, rinsed lentils (brown or green), diced tomatoes (no salt added), and herbs like thyme or bay leaf.
        *   Simmer until lentils are tender (about 30-40 minutes).
        *   Season with black pepper. Add a splash of vinegar or lemon juice at the end if desired.
        *   This soup is high in fiber and protein.
        """
    },
    {
        "id": "doc4",
        "condition": "General Healthy Eating / Weight Management",
        "text": """
        **General Healthy Eating & Weight Management Tips:**

        *Focus on whole, unprocessed foods, portion control, and balanced macronutrients.*

        **Fruits:** Include a variety of colorful fruits daily. Good source of vitamins, minerals, and fiber.
        **Vegetables:** Fill half your plate with non-starchy vegetables at meals (leafy greens, broccoli, peppers, zucchini, etc.). They are nutrient-dense and low in calories.
        **Meats/Proteins:** Choose lean protein sources (chicken, turkey, fish, beans, lentils, tofu, eggs). Protein helps with satiety. Include protein with each meal.
        **Grains:** Opt for whole grains (brown rice, quinoa, oats, whole wheat bread) over refined grains. They provide more fiber and nutrients. Be mindful of portion sizes.
        **Fats:** Include healthy fats from sources like avocados, nuts, seeds, and olive oil. Limit saturated and trans fats found in fried foods, fatty meats, and processed snacks.
        **Other:** Drink plenty of water throughout the day. Limit sugary drinks (soda, juice) and alcohol. Reduce intake of processed foods, fast food, and high-sugar snacks. Practice mindful eating - pay attention to hunger and fullness cues. Regular physical activity is also crucial for weight management and overall health.

        **Simple Recipe Idea: Grilled Chicken Salad**
        *   Grill or pan-sear a chicken breast. Let it rest, then slice or dice it.
        *   Create a large salad base with mixed greens, spinach, cucumber, tomatoes, bell peppers, and red onion.
        *   Add the cooked chicken.
        *   Optional additions: chickpeas, a small amount of sliced avocado, or some sunflower seeds.
        *   Dress with a light vinaigrette made from olive oil, lemon juice or vinegar, and herbs.
        """
    },
    {
        "id": "doc5",
        "condition": "Iron Deficiency Anemia",
        "text": """
        **Diet Recommendations for Iron Deficiency Anemia:**
       
        *Focus on boosting iron intake and enhancing absorption.*
       
        **Fruits:** Citrus fruits (oranges, grapefruit), strawberries, bell peppers, tomatoes (Vitamin C sources eaten with iron-rich foods help absorption).
        **Vegetables:** Spinach, kale, broccoli, sweet potatoes, peas.
        **Meats/Proteins:** Lean red meat (beef, lamb), poultry (chicken, turkey - dark meat has more iron), fish (sardines, tuna), eggs, lentils, beans (kidney, chickpeas), tofu, pumpkin seeds.
        **Grains:** Iron-fortified cereals, breads, and pasta; quinoa, oats.
        **Other:** Cook in cast-iron skillets (can add small amounts of iron). Avoid drinking coffee or tea *with* iron-rich meals as tannins can inhibit absorption. Calcium supplements or high-calcium foods (like dairy) can also interfere, so time them separately.
       
        **Simple Recipe Idea: Lean Beef and Broccoli Stir-Fry**
        *   Slice lean beef thinly. Stir-fry in a wok or large pan with a little sesame oil until browned. Remove beef.
        *   Add broccoli florets and sliced red bell peppers (Vit C) to the pan, stir-fry until tender-crisp.
        *   Return beef to the pan. Add a sauce made from low-sodium soy sauce, ginger, garlic, and a touch of orange juice (Vit C).
        *   Serve immediately over brown rice or quinoa.
        """
    },
    {
        "id": "doc6",
        "condition": "GERD / Acid Reflux Management",
        "text": """
        **Diet Recommendations for GERD / Acid Reflux Management:**
        
        *Focus on avoiding common trigger foods, eating smaller meals, and choosing low-fat options.*
        
        **Fruits:** Bananas, melons (cantaloupe, honeydew), pears, apples (non-citrus, in moderation).
        **Vegetables:** Green beans, broccoli, asparagus, cauliflower, potatoes, cucumbers, leafy greens.
        **Meats/Proteins:** Lean poultry (skinless chicken/turkey - baked, grilled, or poached), fish (baked, grilled, or poached), egg whites, tofu.
        **Grains:** Oatmeal, whole-wheat bread, brown rice, couscous.
        **Dairy:** Low-fat or skim milk, low-fat yogurt (plain), small amounts of low-fat cheese (if tolerated).
        **Other:** Healthy fats in moderation (avocado, olive oil). Stay upright after eating, avoid late-night meals. Common triggers to avoid: Citrus fruits, tomatoes/tomato sauce, garlic, onions, spicy foods, fried/fatty foods, chocolate, mint, caffeine (coffee, tea, soda), alcohol, carbonated beverages.
        
        **Simple Recipe Idea: Baked Chicken Breast with Roasted Sweet Potatoes and Green Beans**
        *   Toss cubed sweet potatoes and trimmed green beans with a small amount of olive oil, salt, and pepper (avoid garlic/onion powder if sensitive).
        *   Roast on a baking sheet at 400°F (200°C) for about 20-25 minutes.
        *   Season a skinless chicken breast with salt, pepper, and perhaps some mild herbs like thyme or rosemary. Add to the baking sheet for the last 15-20 minutes of cooking, until chicken is cooked through.
        *   Serve warm.
        """
    },
    {
        "id": "doc7",
        "condition": "Constipation Relief",
        "text": """
        **Diet Recommendations for Constipation Relief:**
        
        *Focus on significantly increasing dietary fiber intake from various sources and ensuring adequate hydration.*
        
        **Fruits:** Prunes, figs, berries (raspberries, blackberries), pears (with skin), apples (with skin), kiwi, oranges.
        **Vegetables:** Broccoli, Brussels sprouts, carrots, leafy greens (spinach, kale), peas, artichokes.
        **Meats/Proteins:** Legumes are excellent fiber sources: Beans (black, kidney, pinto), lentils, chickpeas. Other proteins are generally low in fiber.
        **Grains:** Whole grains are key: Oatmeal (especially steel-cut or rolled), brown rice, quinoa, barley, whole-wheat bread and pasta, bran cereals.
        **Other:** Nuts and seeds (chia seeds, flax seeds, almonds, walnuts - in moderation), plenty of water throughout the day (aim for 8+ glasses). Regular physical activity also helps stimulate bowel movements.
        
        **Simple Recipe Idea: High-Fiber Oatmeal with Berries and Seeds**
        *   Cook rolled oats or steel-cut oats according to package directions using water or milk.
        *   Once cooked, stir in 1-2 tablespoons of chia seeds or ground flax seeds.
        *   Top with a generous handful of fresh berries (like raspberries or blueberries) and a small sprinkle of nuts if desired.
        *   Consider adding sliced prunes for an extra boost.
        """
    },
    {
        "id": "doc8",
        "condition": "Building Muscle / High Protein Diet Support",
        "text": """
        **Diet Recommendations for Building Muscle / High Protein Diet Support:**
        
        *Focus on adequate protein intake distributed throughout the day, paired with complex carbohydrates for energy and sufficient calories overall.*
        
        **Fruits:** All types are beneficial for vitamins, minerals, and antioxidants (e.g., bananas for potassium, berries for antioxidants).
        **Vegetables:** Include a wide variety for micronutrients (e.g., spinach, broccoli, sweet potatoes).
        **Meats/Proteins:** Prioritize lean sources: Chicken breast, turkey breast, lean beef (sirloin, tenderloin), fish (salmon, tuna, tilapia), eggs (whole eggs and egg whites), Greek yogurt, cottage cheese, tofu, edamame, beans, lentils.
        **Grains:** Complex carbohydrates for sustained energy: Oats, quinoa, brown rice, whole-wheat pasta, whole-wheat bread, buckwheat.
        **Dairy:** Greek yogurt, cottage cheese, milk (choose fat level based on overall calorie needs).
        **Other:** Healthy fats (avocado, nuts, seeds, olive oil). Adequate hydration is crucial. Consider protein timing around workouts (e.g., a meal or snack with protein and carbs within a couple of hours post-exercise).
        
        **Simple Recipe Idea: Grilled Chicken Breast with Quinoa and Steamed Asparagus**
        *   Cook quinoa according to package directions.
        *   Grill or pan-sear a seasoned chicken breast until cooked through.
        *   Steam or lightly sauté asparagus spears with a little olive oil, salt, and pepper.
        *   Serve the chicken breast alongside a portion of quinoa and asparagus for a balanced, high-protein meal.
        """
    },
    {
        "id": "doc9",
        "condition": "Low FODMAP Diet (Initial Phase Example for IBS Symptoms)",
        "text": """
        **Diet Recommendations for Low FODMAP Diet (Initial Phase for IBS Symptoms):**
        
        *Focus: Temporarily restrict high-FODMAP carbohydrates to identify potential IBS triggers. IMPORTANT: This diet is complex and meant to be short-term, followed by systematic reintroduction under professional guidance (doctor or registered dietitian specializing in IBS). This is just an example of *some* low-FODMAP foods.*
        
        **Fruits (Low FODMAP examples):** Unripe bananas, blueberries, cantaloupe, grapes, kiwi, lemon, lime, oranges, raspberries, strawberries (limit quantities as per Monash University app guidelines).
        **Vegetables (Low FODMAP examples):** Bell peppers (any color), carrots, cucumber, eggplant, green beans, kale, lettuce, potatoes, spinach, tomatoes, zucchini.
        **Meats/Proteins:** Plain cooked beef, chicken, fish, lamb, pork, shellfish, eggs, firm tofu.
        **Grains:** Gluten-free bread/pasta (check ingredients for high-FODMAP additives), oats, quinoa, rice (white, brown), corn tortillas.
        **Dairy:** Lactose-free milk/yogurt, hard cheeses (cheddar, mozzarella, parmesan), small amounts of butter.
        **Other:** Maple syrup (pure), peanuts, pumpkin seeds, walnuts, olive oil. Avoid: High-FODMAP fruits (apples, pears, mangoes, watermelon), vegetables (onions, garlic, cauliflower, mushrooms, asparagus), wheat, rye, beans, lentils, high-lactose dairy, honey, high-fructose corn syrup, cashews, pistachios.
        
        **Simple Recipe Idea: Simple Baked Salmon with Rice and Steamed Carrots**
        *   Cook white or brown rice according to package directions.
        *   Season a salmon fillet with salt, pepper, lemon juice, and dill (check seasoning blends for onion/garlic).
        *   Bake salmon at 400°F (200°C) for 12-15 minutes, or until cooked through.
        *   Steam sliced carrots until tender.
        *   Serve the salmon with rice and carrots. Drizzle with a little olive oil if desired.
        """
    },
    {
        "id": "doc10",
        "condition": "Heart Health (Post-Event / Prevention)",
        "text": """
        **Diet Recommendations for Heart Health (Post-Event / Prevention):**
        
        *Focus on reducing saturated and trans fats, limiting sodium, increasing fiber (especially soluble fiber), and incorporating omega-3 fatty acids.*
        **Fruits:** Berries (rich in antioxidants), apples (soluble fiber), oranges (potassium, vitamin C), bananas (potassium).
        **Vegetables:** Leafy greens (spinach, kale), broccoli, carrots, tomatoes, bell peppers. Aim for a variety of colors.
        **Meats/Proteins:** Fatty fish high in omega-3s (salmon, mackerel, herring, sardines) at least twice a week. Skinless poultry, legumes (beans, lentils, chickpeas), tofu, nuts (especially walnuts, almonds), seeds (flaxseeds, chia seeds, sunflower seeds).
        **Grains:** Whole grains like oats (contain beta-glucan, a soluble fiber), quinoa, brown rice, barley, whole-wheat bread/pasta.
        **Dairy:** Low-fat or fat-free milk, yogurt, and cheese.
        **Other:** Use olive oil instead of butter or tropical oils. Limit sodium intake by avoiding processed foods, canned soups, salty snacks, and adding salt at the table (use herbs and spices instead). Limit added sugars, sugary drinks, red meat (especially fatty cuts), and processed meats. Avoid trans fats (often listed as 'partially hydrogenated oils').
        
        **Simple Recipe Idea: Mediterranean Chickpea Salad**
        *   Rinse and drain a can of chickpeas (no salt added, if possible).
        *   Chop cucumber, tomatoes, red bell pepper, and red onion (use sparingly if preferred). Add fresh parsley.
        *   Combine chickpeas and vegetables in a bowl.
        *   Make a dressing with olive oil, lemon juice, dried oregano, and black pepper (avoid adding salt).
        *   Toss the salad with the dressing. Can be served on its own, over lettuce, or with a small portion of whole-wheat pita.
        """
    }
]
