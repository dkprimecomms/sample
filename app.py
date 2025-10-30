from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='.')

@app.route("/")
def home():
    # Renders index.html in the same folder as this file
    return render_template("index.html")

if __name__ == "__main__":
    # App Runner provides PORT automatically
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
