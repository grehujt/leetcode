# 61. Rotate List

## Problem
- Given a list, rotate the list to the right by k places, where k is non-negative.

> For example:
> 
> Given 1->2->3->4->5->NULL and k = 2,
> 
> return 4->5->1->2->3->NULL.

## Solution
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        p, num = head, 0
        while p:
            p = p.next
            num += 1
        cnt = k % num
        if cnt == 0:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        p1, p2, idx = head, head, 0
        while p2.next:
            p2 = p2.next
            if idx >= cnt:
                p1 = p1.next
            idx += 1
        p2.next = dummy.next
        dummy.next = p1.next
        p1.next = None
        return dummy.next
```
