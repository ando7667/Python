class SimpleClass():
    def __init__(self, name):
        self.name = name

    def __init__(self):
        print("удаляется объект {} класса SomeClass".format(self.name))


obj = SimpleClass("Jonn")
