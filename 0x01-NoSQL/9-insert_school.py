#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    """
    new_coll =  mongo_collection.insert_one(kwargs)
    return new_coll.inserted_id
