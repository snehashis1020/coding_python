class node:
    def __init__(self,value):
        self.__data = value
        self.__left = None
        self.__right = None
    def compare(self,value):
        if self.__data > value:
            self.__left = insert(self.__left,value)
        else:
            self.__right = insert(self.__right,value)
    
    def traversal(self):
        if self.__left != None:
            self.__left.traversal()
        if self.__right != None:
            self.__right.traversal()
        print(self.__data)

def insert(a,value):
    if a is None:
        return node(value)
    else:
        a.compare(value)
    return a

root = None
a = [3,8,1,4,2,12,6,7]
for val in a:
    root = insert(root,val)
print(root)
root.traversal()
