class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
       new_node = Node(value)
       new_node.next = self.head
       if self.head:
            self.head.prev = new_node
       else:
            self.tail = new_node
       self.head = new_node

    def add_to_end(self, value):
       new_node = Node(value)
       new_node.prev = self.tail
       if self.tail:
            self.tail.next= new_node
       else:
            self.tail = new_node
       self.tail = new_node
       
    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.head.prev
        if self.tail:
            self.tail.prev = None
        else:
            self.head = None

        return removed_value
       
dll = DoublyLinkedList()

# Add elements to the front and end
dll.add_to_front(3)
dll.add_to_front(2)
dll.add_to_front(1)
dll.add_to_end(4)
dll.add_to_end(5)

# Forward: [1, 2, 3, 4, 5]
# Backward: [5, 4, 3, 2, 1]

# Remove elements from the front and end
print(dll.remove_from_front())  # Removes 1
print(dll.remove_from_end())    # Removes 5
print(dll.remove_from_front())  # Removes 2
print(dll.remove_from_end())    # Removes 4
