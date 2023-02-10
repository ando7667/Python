class StaticMetod():
    @staticmethod
    def hello():
        print("Hello")


    @classmethod
    def hello_world(cls):
        print("Hello World")


StaticMetod.hello()
obj = StaticMetod()
obj.hello()

StaticMetod.hello_world()
