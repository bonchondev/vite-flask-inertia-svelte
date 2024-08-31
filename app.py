from config import PUBLIC_FOLDER, STATIC_FOLDER, TEMPLATES
from flask import Flask, send_from_directory
from flask_inertia import Inertia, render_inertia
from flask_vite import Vite


def create_app() -> Flask:

    app = Flask(
        __name__,
        template_folder=TEMPLATES,
        static_folder=STATIC_FOLDER,
    )

    app.config["INERTIA_TEMPLATE"] = "base.html"
    app.config["SECRET_KEY"] = "changeme"
    app.config["VITE_AUTO_INSERT"] = True
    app.config["VITE_NPM_BIN_PATH"] = "pnpm"

    Inertia(app)

    Vite(app)

    return app


app = create_app()


@app.get("/")
def index():
    return render_inertia("Index")


@app.get("/about")
def about():
    return render_inertia("About", props={"amount": "$7,000"})


@app.post("/data")
def data():
    return {"dollars": 100}


@app.get("/<path:path>")
def static_folder(path):
    return send_from_directory(STATIC_FOLDER, path)


@app.get("/favicon.ico")
def public_folder(path):
    return send_from_directory(PUBLIC_FOLDER, path)


if __name__ == "__main__":
    app.run()
