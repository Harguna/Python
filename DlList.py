class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class Dllist:
    def __init__(self):
        self.head = None


dl = Dllist

#INSERT

#beginning


#end


#mid