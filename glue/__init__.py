from pathlib import Path
from flask import Flask, render_template


# https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Enable development mappings and specify database location
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=Path(app.instance_path, "glue.db")
    )

    # Load test configuration unless an override specified when running create_app
    if config is None:
        app.config.from_pyfile("config.py", silent=True)

    else:
        app.config.from_mapping(config)

    # Ensure instance directory exists
    try:
        Path(app.instance_path).mkdir()

    # TODO: This seems janky
    except OSError as e:
        print(f"Error with app instance_path {app.instance_path}:\n{e}")
        pass

    # TODO: Move these to a routes file
    @app.route("/")
    def handle_root():
        return render_template("home.html")

    @app.route("/about")
    def handle_about():
        about = {
            "root_path": app.root_path,
            "template_path": app.template_folder,
            "env": app.env,
        }

        return render_template("about.html", msg=about, title="About")

    from . import db

    # Add database commands and register close_db with app context teardowns
    db.init_app(app)

    return app
