#!/usr/bin/python3
"""1-fifo_cache.py"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        return self.cache_data.get(key)
