class OtherClass():
    other1 = 42

    def __getattr__(self, item):
        return item.upper()

    # def __getattribute__(self, item):
    #     return item.upper()



obj = OtherClass()

print(obj.other1)
print(obj.other2)
