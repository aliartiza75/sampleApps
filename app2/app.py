import os
from flask import Flask, render_template


FLASK_HOST_IP = os.getenv.get('FLASK_HOST_IP', '0.0.0.0')  # Returns None if the variable is not set
FLASK_HOST_PORT = int(os.environ.get('FLASK_HOST_PORT', 5001))


app = Flask(__name__)


@app.route('/')
def home():
    message = "When in doubt, ﬁsh!"
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True, host=FLASK_HOST_IP, port=FLASK_HOST_PORT)