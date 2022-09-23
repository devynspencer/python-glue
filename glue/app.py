from flask import Flask


app = Flask(__name__)


@app.route("/")
def handle_root():
    return "Everything works, you're incredible."
