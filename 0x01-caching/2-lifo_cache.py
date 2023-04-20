#!/usr/bin/python3
""" LIFO Cache """

from base_caching import BaseCaching
BaseCaching = __import__("base_caching").BaseCaching

class LIFOCache(BaseCaching):
    """ This class represent a LIFO caching system """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.key_order = []

   def remove_last_item(self):
       """ Remove the last item from cache """
       lifo_key = self.key_order.pop()
       del self.cache_data[lifo_key]
       print("DISCARD: {}".format(lifo_key))

   def put(self, key, item):
       """ Add an item in the cache """
       if key is None or item is None:
           return
       if len(self.cache_data) >= self.MAX_ITEMS:
           self.remove_last_item()
       self.cache_data[key] = item
       self.key_order.append(key)
                                                                                                                                                   def get(self, key):
       """ Get an item from the cache """
       if key is None or key not in self.cache_data:
           return None
       self.key_order.remove(key)
       self.key_order.append(key)
       return self.cache_data[key]
