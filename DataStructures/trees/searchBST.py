class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def search(root,key):
    if root == None:
        return False
    if root.info== key:
        return True
    if root.info > key:
        return search(root.left,key)
    else:
        return search(root.right,key)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int,input().split()))

for i in range(t):
    tree.create(arr[i])

key = int(input())
if(search(tree.root,key)):
    print("Hurry, it is in the tree.")
else:
    print("sorry, there is no such element.")
