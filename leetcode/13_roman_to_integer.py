class Solution(object):
  def romanToInt(self, s):
    roman_map = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    result = roman_map[s[0]]
    i = 1
    while i < len(s):
      if roman_map[s[i]] > roman_map[s[i-1]]:
        result += roman_map[s[i]] - (2 * roman_map[s[i-1]])
        i += 1
      else:
        result += roman_map[s[i]]
        i += 1
    
    return result
        