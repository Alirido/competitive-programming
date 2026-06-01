from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)
    if n == 0:
      return None
    elif n == 1:
      return lists[0]
    result = lists[0]
    for i in range(1, n):
      dummy = ListNode()
      tail = dummy
      n1 = result
      n2 = lists[i]
      while n1 and n2:
        if n1.val <= n2.val:
          tail.next = n1
          tail = n1
          n1 = n1.next
        else:
          tail.next = n2
          tail = n2
          n2 = n2.next
      tail.next = n1 if n1 else n2
      result = dummy.next
    return result

class Solution: # using divide & conquer approach
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
      return None

    while len(lists) > 1:
      merged = []
      for i in range(0, len(lists), 2):
        a = lists[i]
        b = lists[i + 1] if i + 1 < len(lists) else None
        merged.append(self.mergeTwo(a, b))
      lists = merged

    return lists[0]

  def mergeTwo(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while a and b:
      if a.val <= b.val:
        tail.next = a
        a = a.next
      else:
        tail.next = b
        b = b.next
      tail = tail.next
    tail.next = a or b
    return dummy.next