#!/usr/bin/env python3
''' List all documents '''


def list_all(mongo_collection):
    ''' List all documents '''
    return [x for x in mongo_collection.find()]
