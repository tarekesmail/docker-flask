from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("This is test task!")

@app.route("/users")
def users():
    return jsonify("this is users list!")

@app.route("/apps")
def apps():
    return jsonify("this is apps list!")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
