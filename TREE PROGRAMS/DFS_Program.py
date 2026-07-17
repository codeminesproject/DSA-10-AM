

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

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)

def searchNode(node,key):
    if node.data==key:
        return node
    for child in node.children:
        result=searchNode(child,key)
        if result is not None:
            return node
    
    return None


response = searchNode(A,"G")
if response is not None:
    print("Node Exist")
else:
    print("Node Not Present")
