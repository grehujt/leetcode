# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heapify, heappop, heapreplace
        dummy = ListNode(0)
        cur = dummy
        h = [(n.val, n) for n in lists if n]
        heapify(h)  # O(n)
        while h:  #O(n)
            _, n = h[0]
            if n.next is None:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, n.next))  # O(log(m))
            cur.next = n
            cur = cur.next
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

a = gen_nodes([])
b = gen_nodes([1])
print 'input1:',
print_nodes(a)
print 'input2:',
print_nodes(b)
print
# c = gen_nodes
t = Solution().mergeKLists([a, b])
print 'result',
print_nodes(t)
