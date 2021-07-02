class Country:

    def __init__(self,name='Default'):
        self.name=name
        print('Constructor')

    # Cannot override constructor. If we do so then we loose default/noarg constructor
    '''
    def __init__(self,name):
        self.name=name
        print('Constructor 2')
    '''

    def instance_method(self):  # neednot be self it can be anyword
        print('instance method')


default=Country()
print(default.name)

india = Country('India')
print(india.name)
