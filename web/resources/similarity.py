import logging
from typing import List, Dict

import spacy
from flask import jsonify, request
from flask_restful import Resource

from resources.validations import check_expected_paramaters
from services.user_updater import decrease_tokens
from services.user_validator import is_valid_user, authenticate, has_tokens


def validations(expected_parameters: List, posted_data: Dict) -> any:
    response = None
    if not check_expected_paramaters(expected_parameters, posted_data):
        response = {
            "status": 308,
            "message": "Invalid parameters"
        }
        return response

    if not is_valid_user(posted_data["username"]):
        response = {
            "status": 301,
            "message": "Invalid username"
        }
        return response

    if not authenticate(posted_data["username"], posted_data["password"]):
        response = {
            "status": 302,
            "message": "Can't login"
        }
        return response

    if not has_tokens(posted_data["username"]):
        response = {
            "status": 303,
            "message": "Need more tokens"
        }
        return response

    return response


class Similarity(Resource):
    def post(self):
        posted_data = request.get_json()
        logging.info('posted_data {0}'.format(posted_data))

        response = validations(["username", "password", "text1", "text2"], posted_data)
        if response is not None:
            return jsonify(response)

        logging.info('valid parameters')
        nlp = spacy.load('es_core_news_sm')
        text1 = nlp(posted_data['text1'])
        text2 = nlp(posted_data['text2'])

        ratio = text1.similarity(text2)

        decrease_tokens(posted_data["username"])

        response = {
            "status": 200,
            "ratio": ratio,
            "message": "Similarity score calculated successfully"
        }
        return jsonify(response)
