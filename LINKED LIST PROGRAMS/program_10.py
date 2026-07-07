
# display value at 2nd position

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

print("display value at 2nd position:")

find_position = 1
position = 0

current = head

while current.next is not None and position <= find_position:
    if position == find_position:
        print(current.data)
        break
    else:
        current = current.next
        position += 1