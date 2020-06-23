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


def pathfetch(node,val,path):
    if (node==None):
        print("Not Found")
    #print (node.data,"  ",val)
    if(node.data==val):
        return path
    elif (node.data>val):
        path.append(node.data)
        path=pathfetch(node.left,val,path)
    else :
        path.append(node.data)
        path=pathfetch(node.right,val,path)
    return path


a=int(input("Enter first value"))
b=int(input("Enter second value"))

aPath=[]
bPath=[]

aPath=pathfetch(root,a,aPath)
bPath=pathfetch(root,b,bPath)


aPath=set(aPath)
bPath=set(bPath)
common=list(aPath&bPath)

commPath=list(reversed(common))
if(len(commPath)>2):
    print(commPath[0],"  ",commPath[1])
else:
    print(commPath[0])
