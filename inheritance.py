class A:
    def sum(self,x,y):
        print(x+y)

    def mul(self,x,y):
        print(x*y)

class B(A):
    #now with this B(A) methode B inherate from A
    def div(self,x,y):
        print(x/y)

obj =B()
obj.div(5,2)