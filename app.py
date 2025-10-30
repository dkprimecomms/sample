from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on AWS App Runner! 🎉"

if __name__ == "__main__":
    # App Runner provides PORT automatically
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
