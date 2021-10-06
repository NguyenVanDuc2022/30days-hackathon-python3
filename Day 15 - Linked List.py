"""
Day 15 - Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor
argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added,
return the reference to the head node.
--- Nguyen Van Duc ---
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


mylist = Solution()
T = int(input("Enter T: "))
head = None
for i in range(T):
    data = int(input("Enter data: "))
    head = mylist.insert(head, data)

mylist.display(head)
