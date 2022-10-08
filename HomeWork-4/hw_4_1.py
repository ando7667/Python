# =========================================================
# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
# ------------------------------------------------------
from decimal import Decimal


def precision(n, s):
    nm = Decimal(n)
    return nm.quantize(Decimal(s))


numb = float(input("Enter a real number: ").replace(",", "."))
st = input("Enter the required accuracy '0.0001': ")

print(precision(numb, st))
