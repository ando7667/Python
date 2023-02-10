class SomeNewClass():
    def __init__(self, value):
        self._value = value


    def getValue(self):
        return self._value

    def setValue(self):
        self._value = value

    def delValue(self):
        del self._value
