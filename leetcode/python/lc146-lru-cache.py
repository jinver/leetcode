# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists 
# in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently used 
# item before inserting a new item.


class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.dict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last=False)
            self.dict[key] = value