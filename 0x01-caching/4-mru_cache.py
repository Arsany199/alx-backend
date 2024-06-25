#!/usr/bin/env python3
"""model of mru class"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """defines mru class"""
    def __init__(self):
        """Initializes the class atribute"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """puts item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                dis_key, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {dis_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get the item by key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return (self.cache_data.get(key, None))
