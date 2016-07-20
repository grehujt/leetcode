# 25. Reverse Nodes in k-Group

## Problem
- Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
- If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
- You may not alter the values in the nodes, only nodes itself may be changed.
- Only constant memory is allowed.

> For example,
> 
> Given this linked list: 1->2->3->4->5
> 
> For k = 2, you should return: 2->1->4->3->5
> 
> For k = 3, you should return: 3->2->1->4->5

## Solution

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, end):
            start, s2 = head.next, head.next
            b2 = end.next
            end.next = None
            pre, cur = start, start.next
            while cur is not None:
                pre.next = cur.next
                cur.next = start
                start = cur
                cur = pre.next
            head.next = start
            s2.next = b2
            return s2

        dummy = ListNode(0)
        dummy.next = head
        i, start, stop = 0, dummy, dummy
        while stop:
            if i == k:
                i = 0
                start = stop = reverse(start, stop)
            else:
                i += 1
                stop = stop.next
        return dummy.next
```
