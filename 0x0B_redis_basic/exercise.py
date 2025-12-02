#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union


class Cache:
    """cache class to store and retrieve data using Redis"""
    def __init__(self):
        """ Initialize the Cache class with a Redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis and return a unique key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
