class WordDictionary:
  def __init__(self):
    self.words = set()

  def addWord(self, word: str) -> None:
    self.words.add(word)

  def search(self, word: str) -> bool:
    indices = [index for index, char in enumerate(word) if char == "."]

    if not indices:
      return word in self.words
    else:
      if len(indices) == 2:
        for x in "abcdefghijklmnopqrstuvwxyz":
          for y in "abcdefghijklmnopqrstuvwxyz":
            tmp = word[:indices[0]] + x + word[indices[0] + 1:indices[1]] + y + word[indices[1] + 1:]
            if tmp in self.words:
              return True
      else:
        for x in "abcdefghijklmnopqrstuvwxyz":
          tmp = word[:indices[0]] + x + word[indices[0] + 1:]
          if tmp in self.words:
            return True
      return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)