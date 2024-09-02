from config import PUBLIC_FOLDER, STATIC_FOLDER, create_app
from flask import send_from_directory
from flask_inertia import render_inertia


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
