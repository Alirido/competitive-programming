from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
      # 1. Find the kth node ahead of group_prev
      kth = group_prev
      for _ in range(k):
        kth = kth.next
        if kth is None:
          return dummy.next     # fewer than k left — done

      group_next = kth.next     # the node after the current group

      # 2. Reverse the group (from group_prev.next to kth)
      prev, curr = group_next, group_prev.next
      while curr is not group_next:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

      # 3. Splice: connect previous group's tail to new group head (kth)
      new_group_tail = group_prev.next    # the original first node — now the tail
      group_prev.next = kth                # new head is kth
      group_prev = new_group_tail          # advance group_prev for next iteration

    return dummy.next

