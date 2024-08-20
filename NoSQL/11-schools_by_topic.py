#!/usr/bin/env python3
"""
this function returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school with a specofic topic
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find({"topics": topic})
