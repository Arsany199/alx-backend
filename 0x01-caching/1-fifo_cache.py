#!/usr/bin/python3
"""model of fifo class"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """the class of fifo cache"""
    def __init__(self):
        """initialize from the parent class"""
        super().__init__()

    def put(self, key, item):
        """put something in the cache"""
        if key != None or item != None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                dis_key = list(self.cache_data.keys())[0]
                del self.cache_data[dis_key]
                print("DISCARD: {}".format(dis_key))
            self.cache_data[key] = item
    def get(self, key):
        """function to get value in self.cache_data"""
        if key == None or key not in self.cache_data.keys():
            return (None)
        return (self.cache_data.get(key))
