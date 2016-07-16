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
        def dc(l):
            mid = len(l) >> 1
            h, t = l[:mid], l[mid:]
            if len(h) > 1:
                h = dc(h)
            if len(t) > 1:
                t = dc(t)

            if len(h) == 0:
                return t
            if len(t) == 0:
                return h
            dummy = ListNode(0)
            cur, n1, n2 = dummy, h[0], t[0]
            while n1 or n2:
                v1 = n1.val if n1 is not None else None
                v2 = n2.val if n2 is not None else None
                if v1 is not None and v2 is not None:
                    if v1 <= v2:
                        cur.next = n1
                        n1 = n1.next
                    else:
                        cur.next = n2
                        n2 = n2.next
                    cur = cur.next
                elif v1 is not None:
                    cur.next = n1
                    break
                else:
                    cur.next = n2
                    break
            return [dummy.next]
        if len(lists) == 0:
            return None
        return dc(lists)[0]


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
