# add node after sanorita node of linked list

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

print("---- add new node with value Santtosh after Sanorita ------------")

current = head

while current.next is not None:
    if current.data=="Sanorita":
        node5 = Node("Santtosh")
        node5.next = current.next
        current.next = node5
        break
    current = current.next

print("--------- display linked list after adding new node at after sanorita --------------------")
current = head

print(current.data)

while current.next is not None:
    current = current.next
    print(current.data)

