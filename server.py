from flask import Flask, render_template, request, make_response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def index():
    if "textToAnalyze" in request.args:
        textToAnalyze = request.args["textToAnalyze"]
        response = emotion_detector(textToAnalyze)

        if response["dominant_emotion"] == "None":
            message = "Invalid text! Please try again!"
        else:
            message = "For the given statement, the system response is 'anger':"+response.anger+" 'disgust' : "+response.disgust+" 'fear' : "+response.fear+" 'joy' : "+response.joy+" 'sadness' : "+response.sadness+". The dominant emotion is "+response.dominant_emotion+"."

        return render_template("index.html", message = message, text = textToAnalyze)
    else:
        return render_template("index.html", message = "", text = "")
