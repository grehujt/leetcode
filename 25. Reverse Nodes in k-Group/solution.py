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
        def rev(start, stop, k):
            while k:
                tmp = start.next
                start.next = stop
                stop = start
                start = tmp
                k -= 1
            return stop, start

        dummy = ListNode(0)
        dummy.next = head
        preHead = None
        cur, cnt = head, 0
        while cur is not None:
            while cur is not None and cnt < k:
                cur = cur.next
                cnt += 1
            if cnt == k:
                beg, end = rev(head, cur, cnt)
                if preHead:
                    preHead.next = beg
                else:
                    dummy.next = beg
                cnt = 0
                preHead = head
                head = cur = end
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
