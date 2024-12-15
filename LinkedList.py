class item:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        node = item(data)
        if(self.head == None):
            self.head = node
            print(f"Added: {data}")
            return
        currNode = self.head
        while (currNode.next != None):
            currNode = currNode.next
        currNode.next = node
        print(f"Added: {data}")
    def printList(self):
        currNode = self.head
        while (currNode.next != None):
            print(currNode.data)
            currNode = currNode.next    
        print(currNode.data)
        

ll = LinkedList()

ll.push("Hello")
ll.push("I")
ll.push("Love")
ll.push("Trains")
ll.printList()