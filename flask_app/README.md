### Shelter Animal Outcomes Web App

This Flask app takes user input on the pet species, age and condition at intake, and predicts the adoption outcome using a trained logistic regression model.

**Files for App**
1. `main.py` - This is the main Python code that uses Flask and calls pet_outcome_prediction.py to use the model
2. `pet_outcome_prediction.py` - This is a separate Python script that reads in the pickled model and also preps the data for the model
3. `logistic_model.p` - a pickled logistic regression model trained on Austin Animal Center Shelter outcome data
4. `index.html` (in a templates folder) - This is the webpage that will be able to take inputs for the model and output a result on the webpage
