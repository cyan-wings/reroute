import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://reuse-assessment.streamlit.app/Evaluate", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
