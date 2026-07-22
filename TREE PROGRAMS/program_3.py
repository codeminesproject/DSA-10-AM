
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

parent_node = searchParentNode(A,"G")
print("Parent Node:",parent_node.data)

for child in parent_node.children:
    if child.data=="G":
        parent_node.children.remove(child)

print("-----------------------------------")

displayTree(A)

