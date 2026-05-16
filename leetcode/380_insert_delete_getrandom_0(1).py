import random
class RandomizedSet(object):
  def __init__(self):
    self.set = set()

  def insert(self, val):
    if val in self.set:
      return False
    self.set.add(val)
    return True

  def remove(self, val):
    if val in self.set:
      self.set.remove(val)
      return True
    return False

  def getRandom(self):
    return random.choice(list(self.set))
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()