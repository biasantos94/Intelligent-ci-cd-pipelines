from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/comprar")
def comprar():
    item = request.args.get("item", "produto")
    return jsonify({"message": f"Pedido realizado: {item}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
