"""Flask app Emotion Detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """This function analyses text from user's query,
    calculates score for each emotion (anger, disgust, fear, joy, sadness)
    and sends a response with explanation emotion dominated."""
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)
    dominant_emotion = result['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system detected the following emotions:<br>"
        f"Anger: {result['anger']}<br>"
        f"Disgust: {result['disgust']}<br>"
        f"Fear: {result['fear']}<br>"
        f"Joy: {result['joy']}<br>"
        f"Sadness: {result['sadness']}<br>"
        f"Dominant Emotion: <strong>{dominant_emotion}</strong> ({result[dominant_emotion]})"
        )


@app.route("/")
def render_index_page():
    """
    Renders the main landing page of the Emotion Detector web application.
    This route handles GET requests to the root URL ("/") and returns the
    'index.html' template, which typically contains the user interface for
    submitting text and viewing emotion analysis results.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
