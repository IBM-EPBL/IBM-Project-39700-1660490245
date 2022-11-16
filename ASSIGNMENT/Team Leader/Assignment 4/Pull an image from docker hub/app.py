from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return("Skill and Job Recommender!")

if __name__=="__main__":
    port = os.environ.get("PORT",5000)
    app.run(port=port,host="0.0.0.0")