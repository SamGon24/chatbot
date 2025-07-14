from flask import Flask, render_template, request
import spacy 

# We initialize spacy 

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")  # Here we load the spacy model to use

@app.route('/')
def index():
    return render_template('index.html')  # Here we render the homepage

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']  # User message
    response = process_mensaje(user_message)  # Process the messsage
    return response  # bot response

# Main logic
def process_mensaje(mensaje):
    doc = nlp(mensaje.lower())  # Converts the message to low caps

    # Responds based on specific key facts
    if "routine" in mensaje or "exercise" in mensaje:
        return "How many days a week would you like to workout"
    elif "nutrition" in mensaje or "food" in mensaje:
        return "Do you have any preference or dietary restriccion"
    else:
        return "Hey! I am your virtual fitness coach. How can I help you today?"

if __name__ == '__main__':
    app.run(debug=True)