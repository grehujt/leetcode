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
        def reverse(start, end):
            pre, cur = start, start.next
            while cur is not None:
                pre.next = cur.next
                cur.next = start
                start = cur
                cur = pre.next

        dummy = ListNode(0)
        dummy.next = head
        i, start, stop = 0, dummy, dummy
        while stop:
            if i == k:
                i = 0
                beg, end, next = start.next, stop, stop.next
                end.next = None
                reverse(beg, end)
                new = start.next
                start.next.next = next
                start.next = stop
                start, stop = new, new
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
t = Solution().reverseKGroup(a,4)
print 'result',
print_nodes(t)
