# 82. Remove Duplicates from Sorted List II

## Problem
- Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

> For example,
> 
> Given 1->2->3->3->4->4->5, return 1->2->5.
> 
> Given 1->1->1->2->3, return 2->3.

## Solution
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if pre.val != cur.val and (cur.next is None or cur.val != cur.next.val):
                pre.next = cur
                pre = cur
                cur = cur.next
                pre.next = None
            else:
                cur = cur.next.next
        return dummy.next
```
