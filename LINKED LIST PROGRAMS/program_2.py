

# add node at end of linked list

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

print("--------- display exisying linked list --------------------")
current = head

print(current.data)

while current.next is not None:
    current = current.next
    print(current.data)

print("------- add Node with data Santtosh after last node in Linked List ------------")

current = head

while current.next is not None:
    current = current.next

node5 = Node("Santtosh")
current.next = node5

print("--------- display linked list after adding new node at end --------------------")
current = head

print(current.data)

while current.next is not None:
    current = current.next
    print(current.data)