''' This function initiates the application EmotionDetection
    The application will be deployed on localhost:5000.
'''

from flask import  Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion over it using emotion_detector()
        function. The output returned shows the labels and their emorion score
        for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    # 'textToAnalyze' is defined in the JS file mywebscript.js
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Check if the label is None, indicating an error or invalid input
    if None in (anger, disgust, fear, joy, sadness, dominant_emotion):
        return {"error": "Emotion detection failed. Please try again with different input."}, 500

    # Return a formatted string with the sentiment label and score
    return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
    }

#Main route to port 5000
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
        It simply runs the render_template function on the HTML template, index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= False)
