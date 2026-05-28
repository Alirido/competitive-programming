class Solution:
  def intToRoman(self, num: int) -> str:
    result = ""
    i = 0
    while num > 0:
      digit = num % 10
      if digit > 0:
        if i == 0:
          match digit:
            case 1:
              result = "I" + result
            case 2:
              result = "II" + result
            case 3:
              result = "III" + result
            case 4:
              result = "IV" + result
            case 5:
              result = "V" + result
            case 6:
              result = "VI" + result
            case 7:
              result = "VII" + result
            case 8:
              result = "VIII" + result
            case 9:
              result = "IX" + result
        elif i == 1:
          match digit:
            case 1:
              result = "X" + result
            case 2:
              result = "XX" + result
            case 3:
              result = "XXX" + result
            case 4:
              result = "XL" + result
            case 5:
              result = "L" + result
            case 6:
              result = "LX" + result
            case 7:
              result = "LXX" + result
            case 8:
              result = "LXXX" + result
            case 9:
              result = "XC" + result
        elif i == 2:
          match digit:
            case 1:
              result = "C" + result
            case 2:
              result = "CC" + result
            case 3:
              result = "CCC" + result
            case 4:
              result = "CD" + result
            case 5:
              result = "D" + result
            case 6:
              result = "DC" + result
            case 7:
              result = "DCC" + result
            case 8:
              result = "DCCC" + result
            case 9:
              result = "CM" + result
        elif i == 3:
          match digit:
            case 1:
              result = "M" + result
            case 2:
              result = "MM" + result
            case 3:
              result = "MMM" + result
      i += 1
      num //= 10
    return result
