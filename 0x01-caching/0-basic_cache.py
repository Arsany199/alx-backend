#!/usr/bin/env python3
"""Create a class BasicCache"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """summary"""

    def __init__(self):
        """summary"""
        super().__init__()

    def put(self, key, item):
        """summary"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
