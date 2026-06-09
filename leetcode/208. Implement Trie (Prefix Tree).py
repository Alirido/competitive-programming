class Trie:
  def __init__(self):
    self.words = set()

  def insert(self, word: str) -> None:
    self.words.add(word)

  def search(self, word: str) -> bool:
    return word in self.words

  def startsWith(self, prefix: str) -> bool:
    for word in self.words:
      n = len(prefix)
      if prefix == word[:n]:
        return True
    return False

# Real Trie data structure:
class TrieNode:
  def __init__(self):
    self.children = {}      # char -> TrieNode
    self.is_end = False     # marks the end of an inserted word

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.is_end = True

  def search(self, word: str) -> bool:
    node = self._find(word)
    return node is not None and node.is_end

  def startsWith(self, prefix: str) -> bool:
    return self._find(prefix) is not None

  def _find(self, s: str):
    node = self.root
    for c in s:
      if c not in node.children:
        return None
      node = node.children[c]
    return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)