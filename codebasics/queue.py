"""
Queue in Python
Adapted from Youtube codebasics 
Title: "Queue - Data Structures & Algorithms Tutorials In Python #8"
URL: https://youtu.be/rUUrmGKYwHw
"""

from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def __repr__(self):
        return "queue([" + ", ".join([str(element) for element in self.container]) + "])"

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return False if self.container else True

    def size(self):
        return len(self.container) 


q1 = Queue()


q1.enqueue(5)
q1.enqueue(8)
q1.enqueue(10)

q1.dequeue()

print(q1)
