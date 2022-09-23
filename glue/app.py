import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def handle_root():
    return render_template("base.html", msg="Everything works, you're incredible.")


@app.route("/about")
def handle_about():
    about = {
        "root_path": app.root_path,
        "template_path": app.template_folder,
        "env": app.env,
    }

    return render_template("base.html", msg=about, title="About")



if __name__ == "__main__":
    app.run(debug=True)
