import json
from flask import Flask


app = Flask(__name__)


@app.route("/")
def handle_root():
    return "Everything works, you're incredible."


@app.route("/about")
def handle_about():
    about = {
        "root_path": app.root_path,
        "template_path": app.template_folder,
        "env": app.env,
    }

    return json.dumps(about)


if __name__ == "__main__":
    app.run(debug=True)
