#!/usr/bin/env python3

"""9-insert_school.py"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.
    """
    if mongo_collection is None:
        return None
    new_doc = mongo_collection.insert_one(kwargs).inserted_id
    return new_doc
