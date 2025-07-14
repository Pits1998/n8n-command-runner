from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Command Runner is Live"

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    cmd = data.get("command")
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return jsonify({"output": output.decode("utf-8")})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode("utf-8")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
