
# remove node at position 2 from linked list

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

print("display existing linked list:")

current = head

linked_list = current.data+" --------> "

while current.next is not None:
    current = current.next
    if current.next is None:
        linked_list += current.data
    else:
        linked_list += current.data+" --------> "

print(linked_list)

print("remove node at position 2 from linked list:")

current = head

remove_position = 2
position = 0

while current.next is not None and position <= remove_position:
    if position != remove_position:
        current = current.next
        position += 1
    else:
        current.next = current.next.next

        

