#!/usr/bin/python3
"""2-lifo_cache.py"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        return self.cache_data.get(key)
