from flask import Flask
from flask_restful import Api

from resources.refill import Refill
from resources.register import Register
from resources.similarity import Similarity


def initialize_application():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Register, "/register")
    api.add_resource(Similarity, "/similarity")
    api.add_resource(Refill, "/refill")
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    initialize_application()
