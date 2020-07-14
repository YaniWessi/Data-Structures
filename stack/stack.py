
from singly_linked_list import LinkedList
import sys
sys.path.append('./single_linked_list')


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# this for the pull request

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if len(self.storage) > 0:
#             self.storage.pop()
#             self.size -= 1
#             return self.storage.pop()


# def pop(self):
#    if not self.size:
#          return None
#
#     self.size -= 1
#     return self.storage.pop()

class Stack:
    def __inite__(self):
        self.size = 0
        self.storage = LinkedList

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.tail.append(value)
        self.size += 1

    def pop(self):
        if not self.size:
            return None

        self.size -= 1
        return self.storage.tail.pop()
