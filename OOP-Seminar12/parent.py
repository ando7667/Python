class Parent():
    def __init__(self):
        print("Paren init")

    def method(self):
        print("parent.method")

class Child(Parent):
    def __init__(self):
        super().__init__()

    def method(self):
        super().method()


child = Child()
print(child.method())