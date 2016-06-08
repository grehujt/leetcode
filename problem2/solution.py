# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur1 = l1
        cur2 = l2
        head = ListNode(-1)
        curNode = head
        while cur1 is not None or cur2 is not None:
            v1 = cur1.val if cur1 is not None else 0
            v2 = cur2.val if cur2 is not None else 0
            v = v1 + v2 + carry
            carry = 1 if v > 9 else 0 
            newNode = ListNode(v - 10 if v > 9 else v)
            curNode.next = newNode
            curNode = newNode
            cur1 = cur1.next if cur1 is not None else cur1
            cur2 = cur2.next if cur2 is not None else cur2
        if carry != 0:
            curNode.next = ListNode(carry)
        return head.next
