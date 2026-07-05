from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    first_dummy = ListNode()
    second_dummy = ListNode()
    first_tail = first_dummy
    second_tail = second_dummy
    while head:
      if head.val < x:
        first_tail.next = head
        first_tail = head
      else:
        second_tail.next = head
        second_tail = head
      head = head.next

    first_tail.next = second_dummy.next
    second_tail.next = None
    return first_dummy.next