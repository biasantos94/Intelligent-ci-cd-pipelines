from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/status")
def status():
    return jsonify({"message": "API funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
