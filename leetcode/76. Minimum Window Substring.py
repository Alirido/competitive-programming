from collections import Counter

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    need = Counter(t)
    left = 0
    right = len(t)
    seen = Counter(s[left:right])
    if need == seen:
      return s[left:right]
    best = ""
    while right < len(s) and left < right:
      if s[right] in seen:
        seen[s[right]] += 1
      else:
        seen[s[right]] = 1
      if need <= seen:
        if best:
          best = min(best, s[left:right + 1], key=len)
        else:
          best = s[left:right + 1]
        seen[s[left]] -= 1
        left += 1
        while need <= seen:
          if not best or right - left + 1 < len(best):
              best = s[left:right + 1]
          seen[s[left]] -= 1
          left += 1

      right += 1
    return best

class Solution: # Alternative better solution because avoiding "Counter <= Counter" comparisons which re-check each character over & over again
  def minWindow(self, s: str, t: str) -> str:
    if not s or not t:
      return ""
    need = Counter(t)
    missing = len(t)          # total chars still needed (with multiplicity)
    left = 0
    best = ""
    for right, c in enumerate(s):
      if need[c] > 0:
        missing -= 1
      need[c] -= 1
      # window valid: shrink from the left as much as possible
      while missing == 0:
        if not best or right - left + 1 < len(best):
          best = s[left:right + 1]
        need[s[left]] += 1
        if need[s[left]] > 0:
          missing += 1
        left += 1
    return best
