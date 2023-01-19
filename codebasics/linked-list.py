"""
Linked List in Python
Adapted from Youtube codebasics 
Title: "Linked List - Data Structures & Algorithms Tutorials in Python #4"
Link: https://youtu.be/qp8u-frRAnU
"""

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) 
            return
        iterator = self.head 
        while iterator.next: 
            iterator = iterator.next
        iterator.next = Node(data, None) 

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator = self.head 
        while iterator: 
            count += 1
            iterator = iterator.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length(): #Checks if index is in range
            raise Exception("Invalidate index")

        if index == 0:
            self.head = self.head.next #points to next element of head if removing head, Py garbarge collection
            return 
            
        count = 0 #linked list have to manually maintain count
        iterator = self.head
        while iterator and count < index - 1: #stop at the previous element
            count += 1
            iterator = iterator.next

        iterator.next = iterator.next.next #points to next of next element

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length(): #Checks if index is in range
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return 

        count = 0 
        iterator = self.head
        while iterator and count < index - 1: #modify next pointer of the previous element
            count += 1
            iterator = iterator.next 

        iterator.next = Node(data, iterator.next)
        
    def print(self):
        if self.head is None: #empty linked list
            print("Linked list is empty")
            return
    
        iterator = self.head
        linked_list_str = ""

        while iterator:
            linked_list_str += str(iterator.data) + "-->" #append data of node
            iterator = iterator.next

        print(linked_list_str)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_values([1,4,5,7,8])
    linked_list.print()
    linked_list.insert_at(4, 100)
    linked_list.print()
    linked_list.insert_at_end(12)
    linked_list.print()

