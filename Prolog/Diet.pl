% Define diseases and their dietary recommendations
diet_recommendation(diabetes, 'Low sugar, high fiber, complex carbohydrates, lean proteins, healthy fats').
diet_recommendation(hypertension, 'Low sodium, high potassium, low fat, fruits, vegetables, whole grains').
diet_recommendation(cardiovascular_disease, 'Low saturated fat, low cholesterol, high fiber, omega-3 fatty acids').
diet_recommendation(anemia, 'Iron-rich foods, vitamin C, lean meats, leafy greens, beans').
diet_recommendation(gastroesophageal_reflux_disease, 'Low acidic foods, small frequent meals, avoid spicy foods, avoid caffeine').
diet_recommendation(celiac_disease, 'Gluten-free foods, high fiber, fruits, vegetables, lean proteins').
diet_recommendation(obesity, 'Low calorie, high nutrient density, whole grains, fruits, vegetables, lean proteins').

% Define facts about diseases
disease(diabetes).
disease(hypertension).
disease(cardiovascular_disease).
disease(anemia).
disease(gastroesophageal_reflux_disease).
disease(celiac_disease).
disease(obesity).

% Suggest diet based on disease
suggest_diet(Disease, Recommendation) :-
    diet_recommendation(Disease, Recommendation).

% Example Queries:
% ?- suggest_diet(diabetes, Recommendation).
% ?- suggest_diet(hypertension, Recommendation).
