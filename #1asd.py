class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.prev: Node = None

    def __str__(self):
        return str(self.data)



class ShiftList:
    length = 0

    def __init__(self):
        self.head: Node = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        elif self.length == 1:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = self.head
            self.head.next = new_node
            self.head.prev = new_node

        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node
        self.length += 1

    def out(self):
        current = self.head
        while current.next != self.head:
            print(current.data)
            current = current.next
        print(current.data)

    def pop(self, i):
        counter = 0
        current = self.head

        while counter != i:
            current = current.next
            i += 1

        current.prev.next = current.next
        current.next.prev = current.prev

        return current.data
    def shift_right(self):
        self.head = self.head.prev

    def shift_left(self):
        self.head = self.head.next



circle = ShiftList()
circle.append(5)
circle.append(112311)
circle.append(2314)
circle.append(10)
circle.out()
circle.shift_right()
print()
circle.out()
print()
circle.shift_left()
circle.out()