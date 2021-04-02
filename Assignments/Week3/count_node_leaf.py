class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def getLeafCount(node):
    if node is None:
        return 0 
    if(node.left is None and node.right is None):
        return 1 
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

root_val = int(input())
root = Node(root_val)
while(1):
	node_val = int(input())
	if node_val != 0:
		root.insert(node_val)
	else:
		print(getLeafCount(root))
		break