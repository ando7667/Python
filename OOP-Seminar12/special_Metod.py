class Special():
    def __new__(cls):
        print("new")
        return super(Special, cls).__new__(cls)

    def __init__(self):
        print("INIT")


obj = Special()
print(obj)
