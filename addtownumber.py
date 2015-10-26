class Node:
    def __init__(self, x):
        self.value = 0
        self.next = None


class Solution:
    def addTwoNumber(self, lst1, lst2):
        dummy = cur = Node(0)
        carry = 0
        if lst1 is None:
            return lst2
        if lst2 is None:
            return lst1
        while lst1 or lst2 or carry >0:
            if lst1:
                a = lst1.value
                lst1 lst1.next
            if lst2:
                b = lst2.value
                lst2 = lst2.next
            sum1 = a + b
            cur.next = ListNode(sum1 % 10)
            carry = sum1/10
            cur = cur.next
        return dummy.next