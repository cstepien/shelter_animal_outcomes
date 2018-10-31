from flask import Flask, request, render_template
from pet_outcome_prediction import pet_outcome

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/pet_outcome/', methods=['GET', 'POST'])
def render_message():

    # user-entered pet info:
    pet_characteristics = ['cat_dog', 'age', 'is_sick']

    # error messages to ensure correct units of measure
    messages = ["Please enter 'cat' or 'dog' only.",
                "The pet age must be in days.",
                "Please enter 'good' or 'bad'."]


    # pet_info = []
    amounts = []

    # takes user input and ensures it can be turned into a floats

    for i, ing in enumerate(pet_characteristics):
        user_input = request.form[ing]
        amounts.append(user_input)

    # show user final message
    final_message = pet_outcome(amounts)
    return render_template('index.html', message=final_message)


if __name__ == '__main__':
    app.run(debug=True)
