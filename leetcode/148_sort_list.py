from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution: # using merge sort algorithm
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
      return head

    # 1. Split the list into two halves using slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    mid = slow.next
    slow.next = None    # cut the list

    # 2. Recursively sort each half
    left = self.sortList(head)
    right = self.sortList(mid)

    # 3. Merge the two sorted halves
    return self.merge(left, right)

  def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
      if l1.val <= l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
