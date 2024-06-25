#!/usr/bin/env python3
"""model for class BasicCache"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """difine the basicCache class"""

    def __init__(self):
        """initialize from the parent class"""
        super().__init__()

    def put(self, key, item):
        """adds item in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
