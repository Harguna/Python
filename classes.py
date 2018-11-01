"""
class Boy:
    gender = "male"

    def __init__(self):
        print("Inside Boy Block")

    def eats(self):
        self.food = "burger"
        print("I ate",self.food)
"""
#a =Boy()
#a.eats()
#a.eats()

class Car():
    tyres = 4
    windows = 6
    name = 'pqr'
    #def __init__(self):
     #   print("Inside Car Block")  t

    def __init__(self,name):
        #self.name='abc'
        print("Self-Name is ",self.name)
        print("Name is ", name)
        #print("Tyres",tyres)          <-- doesnt work
        #print("Self Tyres",self.tyres)

    def speed(self,name):
        self.name=name
        print("Speed of ",self.name)

#a = Car("Aventador")
b= Car('xyz')
b.speed('hhh')
#print (b.name)
#print(a.name)

