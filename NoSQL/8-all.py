#!/usr/bin/env python3
"""
this function lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
