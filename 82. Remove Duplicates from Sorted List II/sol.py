class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        tmp = None
        while cur:
            if tmp != cur.val and (cur.next is None or cur.val != cur.next.val):
                pre.next = cur
                pre = cur
            tmp = cur.val
            cur = cur.next
            pre.next = None
        return dummy.next
