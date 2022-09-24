import json
from flask import Flask, render_template, url_for
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def handle_root():
    return render_template("main.html", msg="Everything works, you're incredible.")


@app.route("/about")
def handle_about():
    about = {
        "root_path": app.root_path,
        "template_path": app.template_folder,
        "env": app.env,
    }

    return render_template("main.html", msg=about, title="About")


@app.route("/ideas")
def handle_ideas():
    ideas = [
        {
            "title": "First Idea Here",
            "content": "Description of idea and steps/links",
            "tags": ["example", "idea", "foo"],
            "author": "Devyn",
            "created": str(datetime.now()),
        },
        {
            "title": "System-generated Idea Here",
            "content": "Description of idea and steps/links",
            "tags": ["example", "idea", "bar"],
            "author": "System",
            "created": str(datetime.now()),
        },
        {
            "title": "Second Idea Here",
            "content": "Description of idea and steps/links",
            "tags": ["example", "idea", "baz"],
            "author": "Devyn",
            "created": str(datetime.now()),
        },
    ]

    return render_template("main.html", ideas=ideas, title="Ideas")


if __name__ == "__main__":
    app.run(debug=True)
