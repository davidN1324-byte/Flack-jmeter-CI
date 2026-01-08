from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/fast")
def fast():
    return jsonify(
        endpoint="fast",
        status="ok"
    ), 200


@app.route("/slow")
def slow():
    time.sleep(1.5)  # имитация долгой операции
    return jsonify(
        endpoint="slow",
        delay="1.5s",
        status="ok"
    ), 200


@app.route("/unstable")
def unstable():
    if random.random() < 0.3:  # ~30% ошибок
        return jsonify(
            endpoint="unstable",
            status="error"
        ), 500

    return jsonify(
        endpoint="unstable",
        status="ok"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)