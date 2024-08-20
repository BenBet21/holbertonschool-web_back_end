#!/usr/bin/env python3
"""
this function inserts a new document in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a new document in a collection based on kwargs
    """
    if mongo_collection is None:
        return []
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
