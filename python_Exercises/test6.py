
#Polymorphisim is achieved through below
# 1) Duck typing
# 2) Operator overloading
# 3) Method overloading
# 4) Method overriding

#Below is an example of duckTyping

class PyCharm:
    def execute(self):
        print('Pycharm')
class MyEditor:

    def execute(self):
        print('MyEditor')

class Laptop:

    def code(self,ide):
        ide.execute()

ide=MyEditor()
ide2=PyCharm()
lap1=Laptop()

#ide or ide2 should have execute method  which means ducktyping
lap1.code(ide2)
