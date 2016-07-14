# 19. Remove Nth Node From End of List

## Problem
- Given a linked list, remove the n-th node from the end of list and return its head.
- Given n will always be valid.
- Try to do this in one pass.

> For example,
> 
>    Given linked list: 1->2->3->4->5, and n = 2.
> 
>    After removing the second node from the end, the linked list becomes 1->2->3->5.

## Solution

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = []
        cur = head
        while cur:
            tmp.append(cur)
            cur = cur.next
        l = len(tmp)
        if n == l:
            return head.next
        elif n == 1:
            tmp[-2].next = None
            return head
        else:
            tmp[l-n-1].next = tmp[l-n+1]
            return head
```
