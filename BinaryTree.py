class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def printTree(self):
        print(self.data)
        if self.left != None:
            self.left.printTree()
        if self.right != None:
            self.right.printTree()
    def addNode(self, data):
        if data <= self.data:
            if self.left == None:
                self.left = node(data)
            else:
                self.left.addNode(data)
        if data > self.data:
            if self.right == None:
                self.right = node(data)
            else:
                self.right.addNode(data)
        
        

class binaryTree:
    def __init__(self):
        self.root = None
    def printTree(self):
        if self.root != None:
            self.root.printTree()
    def addNode(self, data):
        if(self.root == None):
            self.root = node(data)
        else:
            self.root.addNode(data)

bt = binaryTree()
bt.addNode(5)
bt.addNode(4)
bt.addNode(7)
bt.addNode(3)
bt.addNode(2)
bt.addNode(6)
bt.addNode(1)
bt.addNode(8)
bt.printTree()