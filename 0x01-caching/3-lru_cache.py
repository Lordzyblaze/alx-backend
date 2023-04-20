#!/usr/bin/python3
"""
LRU caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU cache implementation
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            lru_key = self.lru_keys.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        if key in self.lru_keys:
            self.lru_keys.remove(key)
        self.lru_keys.append(key)
                                                                                                                            def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_keys.remove(key)
        self.lru_keys.append(key)
        return self.cache_data[key]
