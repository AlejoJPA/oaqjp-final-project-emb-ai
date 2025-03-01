''' This function initiates the application EmotionDetection
    The application will be deployed on localhost:5000.
'''

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' Receives the text from the HTML interface and runs emotion detection
        using emotion_detector(). Returns emotion scores or an error message.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Debugging: Print response to ensure correct handling
    print("DEBUG: Response received:", response)

    # If response is empty (API returned 400) or dominant_emotion is None, return error message
    if not response or response.get("dominant_emotion") is None:
        print("DEBUG: Returning Invalid Text message")  # Debugging
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Extract the label and score from the response
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Return a formatted response
    return (
        f"For the given statement, the system response is:\n"
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},\n"
        f"'joy': {joy} and 'sadness': {sadness},\n"
        f"The dominant emotion is {dominant_emotion}."
    )

# Main route to port 5000
@app.route("/")
def render_index_page():
    ''' Renders the main application page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
