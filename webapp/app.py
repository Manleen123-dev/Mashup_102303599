import os
import sys

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, send_file
from src.mashup import create_mashup

app = Flask(__name__)

OUTPUT_DIR = "data/output"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create():

    singer = request.form["singer"]

    count = int(request.form["count"])

    duration = int(request.form["duration"])

    email = request.form["email"]

    # define filename properly
    filename = "mashup.mp3"

    try:

        output_path = create_mashup(
            singer,
            count,
            duration,
            filename
        )

        return render_template(
            "index.html",
            success=True,
            filename=filename
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

