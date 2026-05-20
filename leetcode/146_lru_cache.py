from collections import OrderedDict

class LRUCache:
  def __init__(self, capacity: int):
    self.cache = OrderedDict()
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    self.cache.move_to_end(key)        # mark as most recently used
    return self.cache[key]

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.cache.move_to_end(key)      # update position
    self.cache[key] = value             # insert or overwrite
    if len(self.cache) > self.capacity:
      self.cache.popitem(last=False)    # evict least recently used
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)