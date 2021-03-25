from collections import *


def read(str='i'):  # return read("int")
    if(str == "float"):
        return map(float, input().split())
    return map(int, input().split())


def ReadArr():
    return [int(x) for x in input().split()]


class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree(object):#Class cây tìm kiếm nhị phân.
    """docstring for Tree"""

    def __init__(self):
        self.root = None

    def insert(self, val): #Hàm insert dùng để thêm 1 phần tử vào cây.
        if self.root is None:
            self.root = Node(val)
            return
        else:
            temp = self.root
            while temp:
                if temp.data == val:
                    return
                elif temp.data > val:
                    if temp.left is None:
                        temp.left = Node(val)
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(val)
                    else:
                        temp = temp.right

    def __countHeight__(self, root): #Thủ tục đệ quy tính chiều cao của cây.
        if root is None: # nếu node rỗng thì trả về giá trị 0
            return 0

        left = self.__countHeight__(root.left) + 1 # Duyệt chiều cao node bên trái
        right = self.__countHeight__(root.right) + 1 # Duyệt chiều cao node bên phải.
        return max(left, right) # Chiều cao lớn nhất của 2 nhánh sẽ là chiều cao của cây.

    def countHeigh(self):# Gọi thủ tục đệ quy trả lời truy vấn chiều cao của cây.
        return self.__countHeight__(self.root)


if __name__ == '__main__':
    T = Tree()
    Q = deque()
    check = [0]*1000
    while True:
        a = ReadArr()
        if a[0] == 3:
            break
        elif a[0] == 0:
            Q.appendleft(a[1])
            check[a[1]] = 1
        elif a[0] == 1:
            Q.append(a[1])
            check[a[1]] = 1
        else:
            if check[a[1]]:
                Q.insert(Q.index(a[1])+1, a[2])
            else:
                Q.append(a[2])
    for x in Q:
        T.insert(x)
    print(T.countHeigh())