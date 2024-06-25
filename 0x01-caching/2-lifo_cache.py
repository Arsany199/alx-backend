#!/usr/bin/python3
"""model of lifo class"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """the class of lifo cache"""
    def __init__(self):
        """initialize from the parent class"""
        super().__init__()

    def put(self, key, item):
        """put something in the cache"""
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                dis_key = list(self.cache_data.keys())[-1]
                del self.cache_data[dis_key]
                print(f"DISCARD: {dis_key}")
            self.cache_data[key] = item

    def get(self, key):
        """function to get value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return (None)
        return (self.cache_data.get[key])
