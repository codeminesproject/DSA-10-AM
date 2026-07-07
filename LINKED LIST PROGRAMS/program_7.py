# remove last node from linked list

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

print("display exisying linked list:")

current = head

linked_list = current.data+" --------> "

while current.next is not None:
    current = current.next
    if current.next is None:
        linked_list += current.data
    else:
        linked_list += current.data+" --------> "

print(linked_list)

print("remove first node from linked list:")

current = head

head = current.next

print("display linked list after removing first node:")

current = head

linked_list = current.data+" --------> "

while current.next is not None:
    current = current.next
    if current.next is None:
        linked_list += current.data
    else:
        linked_list += current.data+" --------> "

print(linked_list)