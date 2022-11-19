class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end="->")
            temp = temp.next

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, index):
        if self.head == None:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next


# Linked list
llist = LinkedList()
llist.head = Node(44)
llist.append(36)
llist.append(90)
llist.append(10)
llist.append(60)
llist.append(99)
llist.printList()
print()
print("Insert 104")
llist.insert(104)
llist.printList()
print()
print("Append 57")
llist.append(57)
llist.printList()
print()
print("Delete index = 4")
llist.deleteNode(4)
llist.printList()
