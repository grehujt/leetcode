# 24. Swap Nodes in Pairs

## Problem
- Given a linked list, swap every two adjacent nodes and return its head.
- Your algorithm should use only constant space.
- You may not modify the values in the list, only nodes itself can be changed.

> For example,
> Given 1->2->3->4, you should return the list as 2->1->4->3.

## Solution:

- Iteration in O(n) time and O(1) space:

    ```python
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head is None: return None
            flag, dummy = True, ListNode(0)
            dummy.next = head
            pre, cur, next = dummy, head, head.next
            while next:
                if flag:
                    pre.next = next
                    cur.next = next.next
                    next.next = cur
                    pre = next
                    next = cur.next
                else:
                    pre = cur
                    cur = next
                    next = next.next
                flag = not flag
            return dummy.next
    ```

- Recursion in O(n) time and space:

    This solution is taken from [here](https://discuss.leetcode.com/topic/4351/my-accepted-java-code-used-recursion).

    ```python
    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head is None or head.next is None:
                return head
            n = head.next
            head.next = self.swapPairs(head.next.next)
            n.next = head
            return n
    ```
