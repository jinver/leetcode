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