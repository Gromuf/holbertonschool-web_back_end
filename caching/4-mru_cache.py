#!/usr/bin/python3
"""4-mru_cache.py"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""
    def __init__(self):
        """ Initialize the MRU cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.order:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop()
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
