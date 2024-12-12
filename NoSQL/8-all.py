#!/usr/bin/env python3

"""8-all.py"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    if mongo_collection is None:
        return []
    documents = list(mongo_collection.find())
    return documents
