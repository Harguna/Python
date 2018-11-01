class Stack:
    def __init__(self,r ):
        self.r= r

    stk= []
    limit = 10

    def pu(self, x):
        if (self.r + 1 >= self.limit):
            print('overflow')
        else:
            self.stk.append(x)
            self.r = self.r + 1
    def po(self):
        if self.r==0:
            print('underflow')
        else:
            print(self.stk[self.r-1])
            self.r= self.r - 1

x=Stack(0)
x.pu(1)
x.pu(2)
x.pu(4)

x.po()
x.po()
x.po()

x.po()

print(x.stk)
