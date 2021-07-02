def example_method(mandatory_parameter, default_parameter="Default",
                   *args, **kwargs):
    print(f"""
        mandatory_parameter= {mandatory_parameter} {type(mandatory_parameter)}
        default_parameter={default_parameter} {type(default_parameter)}
        args={args} {type(args)}
        kwargs={kwargs} {type(kwargs)}
""")


example_method(1)
example_method(mandatory_parameter=12)
example_method(12, 34)
example_method(12, "something par", "some1", "some2")
example_method(12, "something par", "some1", "some2", key1="a", key2="b")


example_list = [1, 2, 3, 4, 5]
example_dictionary = {'a': '1', 'b': '2', 'c': '3'}
example_method(*example_list,**example_dictionary)  # unpacking list & dictionary using * , **
