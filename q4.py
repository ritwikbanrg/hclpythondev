class node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        

    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.data),
        if self.right:
            self.right.printTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
                   
        
rootnode=int(input("Enter Root"))
root=node(rootnode)

flag=1
while(flag!=0):
    newnode=int(input("Enter next node"))
    root.insert(newnode)
    flag=int(input("Enter 1 to continue or 0 to stop"))
    
root.printTree()


def height(node): 
        if node is None: 
            return 0 
        else :   
            lheight = height(node.left) 
            rheight = height(node.right)  
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1
            
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.data,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1)
        
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i)

printLevelOrder(root)
