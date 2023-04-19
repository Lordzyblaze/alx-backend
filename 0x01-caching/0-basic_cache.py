#!/usr/bin/python3
""" 0. Basic dictionary
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines cache system
    """

    def put(self, key, item):
        """ add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key. If key is
        None or if the key doesnt exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
