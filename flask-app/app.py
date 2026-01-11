from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route("/health") 
def health(): 
    return {"status": "ok"}, 200


@app.route("/fast")
def fast():
    return jsonify(
        endpoint="fast",
        status="ok"
    ), 200


@app.route("/slow")
def slow():
    time.sleep(2)
    return jsonify(
        endpoint="slow",
        delay="2.5s",
        status="ok"
    ), 200


@app.route("/unstable")
def unstable():
    if random.random() < 0.4:
        return jsonify(
            endpoint="unstable",
            status="error"
        ), 500

    return jsonify(
        endpoint="unstable",
        status="ok"
    ), 200


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json(silent=True)
    if not data:
        return {"error": "empty body"}, 400
    return {"ok": True}, 200


@app.errorhandler(404)
def not_found(e):
    return {"error": "not found"}, 404


@app.errorhandler(400)
def bad_request(e):
    return {"error": "bad request"}, 400


@app.route("/validate")
def validate():
    limit = request.args.get("limit", type=int)
    if limit is None or limit < 0:
        return {"error": "invalid limit"}, 400
    return {"limit": limit}, 200






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)