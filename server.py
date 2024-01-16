from flask import Flask, render_template, request, make_response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def index():
    if "textToAnalyze" in request.args:
        textToAnalyze = request.args["textToAnalyze"]
        response = emotion_detector(textToAnalyze)
        return render_template("index.html", resp = response, text = textToAnalyze)
    else:
        response = {'anger': 0, 'disgust': 0, 'fear':0, 'joy':0, 'sadness':0, 'dominant_emotion': 'None'}
        return render_template("index.html", resp = response, text = "")