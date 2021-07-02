class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

#class B(A)
class B:

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

#class C(B):   multilevel inheritance

#Multilevel inheritance
class C(A,B):
    def feature5(self):
        print("Feature 5 working")

a=A()
a.feature1()
a.feature2()

b=B()
#b.feature1()
b.feature3()

c1=C()
c1.feature5()
c1.feature3()
c1.feature1()