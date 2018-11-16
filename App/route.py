from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
route = Blueprint("route", __name__)
from App.Controller.handler import handler
from App import addScheme

@route.route("/", methods=["GET"])
def home():
    return handler.index("")

@route.route("add", methods=["POST"])
@expects_json(addScheme)
def add():
	return handler.add(request.json)

@route.errorhandler(400)
def bad_request(error):
	return jsonify({"status": False, "message": error.description, "data": []})