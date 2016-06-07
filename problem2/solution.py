# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        cur1 = l1
        cur2 = l2
        v = l1.val + l2.val
        head = ListNode(-1)
        curNode = head
        while cur1 is not None and cur2 is not None:
            v = cur1.val + cur2.val + carry
            if v > 9:
                newNode = ListNode(v - 10)
                carry = 1
            else:
                newNode = ListNode(v)
                carry = 0
            curNode.next = newNode
            curNode = newNode
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1 is None and cur2 is not None:
            if cur2.val + carry > 9:
                while cur2:
                    v = cur2.val + carry
                    if v > 9:
                        newNode = ListNode(v - 10)
                        carry = 1
                    else:
                        newNode = ListNode(v)
                        carry = 0
                    curNode.next = newNode
                    curNode = newNode
                    cur2 = cur2.next
            else:
                cur2.val += carry
                carry = 0
                curNode.next = cur2
        elif cur1 is not None and cur2 is None:
            if cur1.val + carry > 9:
                while cur1:
                    v = cur1.val + carry
                    if v > 9:
                        newNode = ListNode(v - 10)
                        carry = 1
                    else:
                        newNode = ListNode(v)
                        carry = 0
                    curNode.next = newNode
                    curNode = newNode
                    cur1 = cur1.next
            else:
                cur1.val += carry
                carry = 0
                curNode.next = cur1
        if carry == 1:
            curNode.next = ListNode(1)
        return head.next
