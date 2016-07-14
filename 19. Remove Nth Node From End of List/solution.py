# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
