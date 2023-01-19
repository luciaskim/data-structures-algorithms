"""
Stack in Python
Adapted from Youtube codebasics 
Title: "Stack - Data Structures & Algorithms Tutorial In Python #7"
URL: https://youtu.be/zwb3GmNAtFk
"""

from collections import deque
stack1 = deque()

stack1.append("alpha")
stack1.append("bravo")
stack1.append("charlie")
print(stack1)

stack1.pop()
print(stack1)

class Stack:
    def __init__(self):
        self.container = deque()

    def __str__(self):
        return ", ".join(value for value in self.container)

    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return False if self.container else True
    
    def size(self):
        return len(self.container)

stack2 = Stack()

print(stack2.is_empty())

stack2.push("delta")
stack2.push("echo")
stack2.push("foxtrot")
stack2.push("golf")

print(stack2)

stack2.pop()

print(stack2)
print(stack2.is_empty())

