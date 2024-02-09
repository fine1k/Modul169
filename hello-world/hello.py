from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Mykhail Myronov INF2022B 09.02.2024"
