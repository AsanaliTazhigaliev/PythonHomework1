import math
a = input ("First leg length:")
b = input ("Length of the second leg:")
a = float (a)
b = float (b)
c = math.sqrt (a ** 2 + b ** 2)
S = (a * b) / 2
P = a + b + c
print ("Triangle area:% .2f"% S)
print ("Perimeter of triangle:% .2f"% P)