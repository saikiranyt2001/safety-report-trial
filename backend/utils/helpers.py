# Helper functions for AI Safety Platform

import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def split_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def get_cached_report(key):
    return r.get(key)

def cache_report(key, value):
    r.set(key, value, ex=300)
