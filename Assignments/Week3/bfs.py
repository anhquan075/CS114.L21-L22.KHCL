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
    def Breadth_first_search(self,root):
        visited = []
        ketqua = ""
        if root:
            visited.append(root)
            ketqua += str(root.data)
        current = root
        while current :
            if current.left:
                ketqua += " " + str(current.left.data)
                visited.append(current.left)
            if current.right:
                ketqua += " " + str(current.right.data)
                visited.append(current.right)
            visited.pop(0)
            if not visited:
                break
            current = visited[0]
        print(ketqua)
a = int(input())
root = Node(a)
a = int(input())
while a!= 0:
    root.insert(a)
    a = int(input())
root.Breadth_first_search(root)