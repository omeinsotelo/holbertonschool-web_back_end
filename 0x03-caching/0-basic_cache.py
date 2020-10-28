#!/usr/bin/python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
    """

    def put(self, key, item):
        """
        add the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get cache item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
