class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# class B(A):
class B:

    #if B init is not there and we created object of B then it calls init method of A
    def __init__(self):
        #will call initA only if you call using super
        #super().__init__()
        print('in B init')

    def feature1(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

#Follows Method Resolution order(MRO) i.e. from left to right
class C(A,B):

    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature4()


# b=B()
# #b.feature1()
# b.feature3()
c=C()

#Though feature1 is there in both A & B but follows MRO rule
c.feature1()

c.feat()


