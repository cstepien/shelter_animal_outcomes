import pickle
import pandas as pd
import numpy as np

# read in the model
mc_model = pickle.load(open("logistic_model.p", "rb"))


# create a function to take in user-entered amounts and apply the model
def pet_outcome(pet_info, model=mc_model):

    # Transform data to get cat, dog features
    if pet_info[0] in ['cat', 'Cat']:
        cat, dog = 1, 0
    else:
        cat, dog = 0, 1

    age_upon_intake_days = float(pet_info[1])

    if pet_info[2] in ['good', 'Good']:
        intake_status = 0
    else:
        intake_status = 1

    # inputs into the model
    input_df = [[cat, dog, age_upon_intake_days, intake_status]]

    # make a prediction
    prediction = int(mc_model.predict(input_df)[0])

    # return a message
    message_array = ["Predicted outcome: Euthanasia/Transfer",
                     "Predicted outcome: Adoption/Return to Owner"]

    return message_array[prediction]
