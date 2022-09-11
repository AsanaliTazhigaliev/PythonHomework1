import math
a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
c=int(input("Enter third value: "))
p = (a + b + c) / 2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('The area of the triangle is %0.2f' %area)
