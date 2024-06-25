#!/usr/bin/python3
"""model of class LFU"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """defines class LFUCache"""

    def __init__(self):
        """initialize class lfu atrributes"""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """function that adds a key and ites item"""
        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS
                    and key not in self.keys):
                dis_key = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[dis_key]
                del self.uses[dis_key]
                print(f"DISCARD: {dis_key:s}")
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] = self.uses[key] + 1

    def get(self, key):
        """function that gets a key and it's item"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return (self.cache_data[key])
        return (None)

    def findLFU(self):
        """function to find LFU"""
        items = list(self.uses.items())
        freqz = [item[1] for item in items]
        least = min(freqz)

        lfuz = [item[0] for item in items if item[1] == least]
        for i in self.keys:
            if i in lfuz:
                return (i)
