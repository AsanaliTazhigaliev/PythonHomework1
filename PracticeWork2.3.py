import math
a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
c=int(input("Enter third value: "))
d =(b**2)-(4*a*c)
sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))