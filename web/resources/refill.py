import logging

from flask import jsonify, request
from flask_restful import Resource

from resources.validations import check_expected_paramaters
from services.user_updater import update_tokens
from services.user_validator import is_valid_user, is_valid_admin


class Refill(Resource):
    def post(self):
        posted_data = request.get_json()
        logging.info('posted_data {0}'.format(posted_data))
        if not check_expected_paramaters(["username", "admin_pw", "refill"], posted_data):
            response = {
                "status": 308,
                "message": "Invalid parameters"
            }
            return jsonify(response)

        if not is_valid_user(posted_data["username"]):
            response = {
                "status": 301,
                "message": "Invalid username"
            }
            return jsonify(response)

        if not is_valid_admin(posted_data["admin_pw"]):
            response = {
                "status": 304,
                "message": "Invalid admin password"
            }
            return jsonify(response)

        update_tokens(posted_data["username"], posted_data["refill"])

        response = {
            "status": 200,
            "message": "Refill successfully"
        }
        return jsonify(response)
