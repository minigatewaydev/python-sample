class Person:
    def __init__(self, name, age, identity, okname):
        self.name = name
        self.age = age
        self.identity = identity
        self.okname = okname

    def myfunc(self):
        print("Hello my name is " + self.name + self.okname)

def func2():
    return 100

#p1 = Person("John", 36, "test", "test2")
# p1.myfunc()
