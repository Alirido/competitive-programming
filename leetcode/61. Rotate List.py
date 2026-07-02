from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return None
    
    tail = head
    n = 1
    while tail.next:
      tail = tail.next
      n += 1
    k %= n
    if k == 0:
      return head
    else:
      tail.next = head
      new_tail = head
      for i in range(n - k - 1):
        new_tail = new_tail.next
      new_head = new_tail.next
      new_tail.next = None
      return new_head