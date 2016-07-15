# 21. Merge Two Sorted Lists

## Problem
- Merge two sorted linked lists and return it as a new list.
- The new list should be made by splicing together the nodes of the first two lists.

## Solution

- iterative solution:

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        while l1 or l2:
            v1 = l1.val if l1 is not None else None
            v2 = l2.val if l2 is not None else None
            if v1 is not None and v2 is not None:
                if v1 <= v2:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            else:
                cur.next = l1 if v1 is not None else l2
                break
        return head.next
```

- tail recursive solution:

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def cont(cur, l1 ,l2):
            if l1 is None:
                cur.next = l2
                return
            if l2 is None:
                cur.next = l1
                return
            if l1.val <= l2.val:
                cur.next = l1
                cont(cur.next, l1.next, l2)
            else:
                cur.next = l2
                cont(cur.next, l1, l2.next)
        head = ListNode(0)
        cur = head
        cont(cur, l1, l2)
        return head.next
```
