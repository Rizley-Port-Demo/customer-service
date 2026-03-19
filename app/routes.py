from flask import Blueprint, jsonify
main = Blueprint("main", __name__)
@main.route("/")
def index():
    return jsonify({"message": "Hello from Flask!"})
@main.route("/health")
def health():
    return jsonify({"status": "ok"})
