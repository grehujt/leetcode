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

def print_nodes(head):
    while head:
        print head.val,
        head = head.next
    print


def gen_nodes(arr):
    dummy = ListNode(0)
    cur = dummy
    for i in arr:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next

a = gen_nodes([1,2,3,4])
print 'input1:',
print_nodes(a)
print
# c = gen_nodes
t = Solution().reverseKGroup(a,2)
print 'result',
print_nodes(t)
