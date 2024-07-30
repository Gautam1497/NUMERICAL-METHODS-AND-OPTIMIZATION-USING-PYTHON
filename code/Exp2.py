# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Queue Implementation
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.items)

# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

# Example usage:

# Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Stack size:", stack.size())

# Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", list(queue.items))
print("Dequeue:", queue.dequeue())
print("Queue size:", queue.size())

# Linked List
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
