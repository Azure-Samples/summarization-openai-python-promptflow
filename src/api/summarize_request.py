import random

from flask import Blueprint, jsonify, request
bp = Blueprint("names", __name__)
from summarizationapp.summarize import process_input

# route to call summarize prompty that takes in a customer id and a question
@bp.route("/get_response")
def get_response():
    problem = request.args.get("problem")
    result = process_input(problem)
    return jsonify(result)
