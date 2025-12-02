#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment call count"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """cache class to store and retrieve data using Redis"""
    def __init__(self):
        """ Initialize the Cache class with a Redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis and return a unique key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> Union[str, bytes, int, float, None]:
        """ Retrieve data from Redis using the given key """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """ Retrieve string data from Redis using the given key """
        data = self._redis.get(key)
        if data is None:
            return None
        return data.decode('utf-8')

    def get_int(self, key: str) -> Union[int, None]:
        """ Retrieve integer data from Redis using the given key """
        data = self._redis.get(key)
        if data is None:
            return None
        return int(data)
