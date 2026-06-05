class Solution:
  def reverseBits(self, n: int) -> int:
    result = 0
    for _ in range(32):
      result = (result << 1) | (n & 1)   # shift result left, take LSB of n
      n >>= 1                            # drop the bit we just used
    return result

# How it works
# Each iteration:

# result << 1 — shift result left by 1 (makes room for the next bit at the LSB position).
# n & 1 — extract the least significant bit of n.
# OR them together — append that bit to the end of result.
# n >>= 1 — discard the bit we just consumed.
# After 32 iterations, result contains the bits of n in reverse order.