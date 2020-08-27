import logging

from pymongo import MongoClient


class DataBase:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DataBase.__instance is None:
            DataBase()
        return DataBase.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DataBase.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            logging.info("creating database")
            db_client = MongoClient("mongodb://db:27017")
            db = db_client.SimilarityDB
            DataBase.__instance = db
