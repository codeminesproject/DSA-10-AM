
# Prepare Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node("Deepak")
node2 = Node("Sanorita")
node3 = Node("Sandeep")
node4 = Node("Apeksha")

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

"""
Display node of linked list one by one
Traversing a Linked List
Traversal means visiting every node one by one.

"""

current = head

print(current.data)

while current.next is not None:
    current = current.next
    print(current.data)