#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

def log_stats():
    """
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collections = client.logs.ngnix
    totals_coll = log_collections.count_documents({})
    get = log_collections.count_documents({"method": "GET"})
    post = log_collections.count_documents({"method": "POST"})
    put = log_collections.count_documents({"method": "PUT"})
    patch = log_collections.count_documents({"method": "PATCH"})
    delete = log_collections.count_documents({"method": "DELETE"})
    path = log_collections.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{totals_coll} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
