class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

n = int(input("Enter number of elements: "))
root = None
for i in range(n):
    val = int(input("Enter value: "))
    root = insert(root, val)

print("Inorder Traversal:")
inorder(root)
