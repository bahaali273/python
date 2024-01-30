class A:
    def sum(self,x,y):
        print(x+y)


class B:
    def mul(self,x,y):
        print(x*y)

class C(A,B):
    def div(self,x,y):
        print(x/y)
obj =C()
obj.mul(5,2)
