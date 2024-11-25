import os
from flask import Flask, render_template


FLASK_HOST_IP = os.getenv('FLASK_HOST_IP', '0.0.0.0')
FLASK_HOST_PORT = int(os.getenv('FLASK_HOST_PORT', 5000))


app = Flask(__name__)


@app.route('/')
def home():
    message = "There's no such thing as a bad day when you're ﬁshing."
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True, host=FLASK_HOST_IP, port=FLASK_HOST_PORT)