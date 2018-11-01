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

ptr= None
l= Llist()

#length
def length(y):
    if y.head== None:
        print('Empty')
    else:
        current= y.head
        count=1
        while (current.getNext() != None):
            count += 1
            current=current.getNext()
        return count

#at beginning
def insertAtBeg(x):
    if (x.head==None):
        num= int(input())
        temp= Node(num)
        x.head= temp
    else:
        num = int(input())
        temp = Node(num)
        temp.setNext(x.head)
        x.head= temp

#at end
def insertAtEnd(x):
    if (x.head == None):
        num = int(input())
        temp = Node(num)
        x.head = temp
    else:
        current= x.head
        while(current.getNext()!= None):
            current= current.getNext()
        num = int(input())
        temp = Node(num)
        current.setNext(temp)

#in middle
def insertInMid(x):
    pos = int(input())
    if pos<=0 or pos> length(x):
        print('Invalid')
    if pos == 1:
        insertAtBeg(x)
    if pos == length(x):
        insertAtEnd(x)
    else:
        count=0
        current= x.head
        while (count != pos-1):
            current= current.getNext()
            count += 1
        num = int(input())
        temp = Node(num)
        temp.setNext(current.getNext())
        current.setNext(temp)

#DELETE

#beginning
def delAtBeg(x):
    if length(x)==0:
        print('Empty')
    elif length(x)==1:
        x.head= None
    else:
        x.head= x.head.getNext()


#end
def delAtEnd(x):
    sec_last = 0
    if length(x) == 0:
        print('Empty')
    elif length(x) == 1:
        x.head = None
    else:
        current= x.head
        while (current.getNext() != None):
            sec_last= current
            current= current.getNext()
        sec_last.setNext(None)

#middle
def delInMid(x):
    pos= int(input())
    if pos<=0 or pos > length(x):
        print('Invalid')
    elif pos == 1:
        delAtBeg(x)
    elif pos== length(x):
        delAtEnd(x)
    else:
        current= x.head
        count=1
        while (count != pos):
            sec_last= current
            current= current.getNext()
            count += 1
        sec_last.setNext(current.getNext())
