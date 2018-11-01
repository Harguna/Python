class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Llist:
    def __init__(self, head= None):
        self.head= head

class Tail:
    def __init__(self, rear= None):
        self.rear= rear

l= Llist()
for i in range (0,5):
    num= int(input())
    temp= Node(num)
    ptr= temp
    if i==0:
        l.head= temp

