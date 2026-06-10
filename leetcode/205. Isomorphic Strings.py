from typing import List

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    pos = {}
    for i, c in enumerate(s):
      if c not in pos:
        pos[c] = [i]
      else:
        pos[c].append(i)
    idx = [v for v in pos.values()]
    diff = set()
    for v in idx:
      if t[v[0]] in diff:
        return False
      diff.add(t[v[0]])
      check = t[v[0]]
      for i in v[1:]:
        if t[i] != check:
          return False
    return True

class Solution: # swap between characters in s & t
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True
