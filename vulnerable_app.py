from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    return os.popen(f"ping -c 1 {host}").read()

@app.route("/search")
def search():
    q = request.args.get("q")
    return f"Search result for: {q}"

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
