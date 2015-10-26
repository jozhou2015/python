class node:
    def ___init__(self):
        self.value = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.root = None

    def add(self, data):
        newnode = node()

        new_node.value = data
        new_node.next = self.root
        self.root = new_node

    def print_list(self):
        node = self.root
        while node:
            print(node.value)
            node = node.next


    def rev_list(self):
        node = self.root
        new_node = node()
        new_node.value =  node.next.value
        new_node.next = self.root
        self.root = new_node
        while node:
            print(node.value)
            node = node.next

lst = linkedlist()
lst.add(7)
lst.add(9)
lst.add(10)
for i in range(100):
    lst.add(i)
lst.print_list()





