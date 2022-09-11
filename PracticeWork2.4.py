import math
print("1-rectangle, 2-triangle, 3-circle")
figure = input("Select a shape:")
if figure == '1':
    print("The lengths of the sides of the rectangle:")
    a = float(input("a ="))
    b = float(input("b ="))
    print("Area:% .2f" % (a * b))
elif figure == '2':
    print("The lengths of the sides of the triangle:")
    a = float(input("a ="))
    b = float(input("b ="))
    c = float(input("c ="))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Area:% .2f" % s)
elif figure == '3':
    r = float(input("Circle radius R ="))
    print("Area:% .2f" % (math.pi * r ** 2))
else:
    print("?")