class Horse():
    is_horse = True


class Donkey():
    is_donkey = True


class Mult(Horse, Donkey):
    pass

mult = Mult()

print(Mult.is_horse)
print(Mult.is_donkey)
