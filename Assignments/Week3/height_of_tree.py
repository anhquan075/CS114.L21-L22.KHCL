from sys import stdin
from collections import deque

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class bst:
    def __init__(self, root = None):
        self.root = Node(root)

    def insert(self, data, node):
        if (node == None):
            node = Node(data)
            return True
        
        if data < node.data:
            if (node.left == None):
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        elif data > node.data:
            if (node.right == None):
                node.right = Node(data)
            else:
                self.insert(data, node.right)

    def level(self, node):
        if (node == None):  return 0
        return max(self.level(node.left), self.level(node.right)) + 1   

# Driver code
arr = deque()
while True:
    try:
        inp = [int(i) for i in stdin.readline().split()]
        if (inp[0] == 3): 
            break
        elif (inp[0] == 0): 
            arr.appendleft(inp[1])
        elif (inp[0] == 1): 
            arr.append(inp[1])
        elif (inp[0] == 2): 
            if (inp[1] in arr):
                arr.insert(arr.index(inp[1])+1, inp[2])
            else:
                arr.appendleft(inp[2])
    except:
        continue


tree = bst()
root = Node(arr[0])
for i in arr:
    tree.insert(i, root)
print(tree.level(root))
