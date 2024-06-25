#!/usr/bin/env python3
"""model of lru"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """defines LRU class inherits from basecaching"""
    def __init__(self):
        """initialize LRU class from its parent"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """function to put keys in cache"""
        if key is None and item is None:
            pass
        else:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                dis_key = self.usedKeys.pop(0)
                del self.cache_data[dis_key]
                print(f"DISCARD: {dis_key:s}")

    def get(self, key):
        """get keys from the cache"""
        if key is not None and key in self.cache_data:
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
