# library imports
from flask import Flask, render_template, request, jsonify
from sentiment_prediction import *

# define the Flask constructor
app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# handle HTTP POST requests from the client-side form submissions
@app.route('/process', methods=['POST'])
def process():
    text = request.form.get('content','Default_value')

    # handle an invalid user input
    if check_input(text) == False:
        return jsonify({'result': '', 'error': 'Bad user input. Try again.'})

    # run the classification model
    processed_text = sentiment_prediction(text)

    # send the output back to the client-side
    return jsonify({'result': processed_text})

if __name__ == '__main__':
    # launch a builtin server for testing
    # app.run(host='localhost', port=5000, debug=True)

    # launch an externally visible server
    app.run(host='0.0.0.0', port=8000, debug=False)
