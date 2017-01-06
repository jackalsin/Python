class MyClass(object):
    def __init__(self):
        self.name = "myName"
        self._privateName = "my secret name"

    def __eq__(self, other):
        return self.name == other.name


    def __repr__(self):
        return self.name

myObj = MyClass()
print myObj._privateName
