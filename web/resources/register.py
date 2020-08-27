import logging
from typing import List, Dict

from flask import jsonify, request
from flask_restful import Resource

from resources.validations import check_expected_paramaters
from services.user_updater import new_user
from services.user_validator import is_valid_user

logging.basicConfig(level=logging.INFO)


def validations(expected_parameters: List, posted_data: Dict) -> any:
    response = None

    if not check_expected_paramaters(expected_parameters, posted_data):
        response = {
            "status": 308,
            "message": "Invalid parameters"
        }

    if response is None and is_valid_user(posted_data["username"]):
        response = {
            "status": 301,
            "message": "Username already taken"
        }

    return response


class Register(Resource):
    def post(self):
        posted_data = request.get_json()
        logging.info('posted_data {0}'.format(posted_data))
        response = validations(["username", "password"], posted_data)

        if response is not None:
            return jsonify(response)

        new_user(posted_data["username"], posted_data["password"], 6)
        response = {
            "status": 200,
            "message": "Registration successful"
        }
        return jsonify(response)
