class node:
    def __init__(self):
        self.val = None
        self.next = None

class lnklist:
    def __init__(self):
        self.root = None

    def add(self,data):
        newnode= node()
        newnode.val = data
        newnode.next = self.root
        self.root = newnode

    def printlist(self):
        node = self.root
        while node:
            print(node.val)
            node = node.next

    def printlist_recursive(self,root):
        node = self.root
        if not node:
            return
        node = node.next
        node.printlist_recursive()
        print(node.value)

    def reverlist(self):
        newroot = lnklist()
        node = self.root
        while node:
            newroot.add(node.val)
            node = node.next
        return newroot

    def rever_iter(self):
        prev = None
        head = self.root
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev



lst = lnklist()
lst2 = lnklist()
lst3 = lnklist()
lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.printlist()
lst.printlist_recursive()
lst2 = lst.reverlist()
lst2.printlist()
lst3 = lst.rever_iter()
lst3.printlist()



