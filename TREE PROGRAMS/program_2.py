
# add child for node in tree
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")
G = TreeNode("G")

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
F.add_child(G)

def displayTree(node,level=0):
    print(" " * level + "↳ " +node.data)
    for child in node.children:
        displayTree(child,level+1)

def addChildNode(root,node,key):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print("Current Node:",current.data)

        if current.data==node:
            child_node = TreeNode(key)
            current.add_child(child_node)
            return current

        for child in current.children:
            queue.append(child)
    return None

def searchParentNode(root,key):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print("Current Node:",current.data)

        for child in current.children:
            if child.data == key:
                return current
            queue.append(child)
    return None


displayTree(A)

result=addChildNode(A,"B","I")
if result is not None:
    print("child added successfully")
    displayTree(A)
else:
    print("key not present")

