#1
import math
a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
h=int(input("Enter third value: "))

s = (((a**2 + b)*h) / (2*(a-b)+4))

print("s={0:.2f}".format(s))

#2
import math
x=int(input("Enter first value: "))
y=int(input("Enter second value: "))

h = (math.sqrt( math.cos(2*y) + math.sin(4*y) + math.sqrt(math.e**x + math.e**(-x))) / ( ((math.e**-x + math.e**x)**3) + (math.sin(4*y) + math.cos(2*y) -2)**2  )   )

print("H={0:.2f}".format(h))

#3(1)
import math
x=2
y=1

result = (((x**y)**x) + ((x**x)**y) - x**4)
print("result={0:.2f}".format(result))

#3(2)
import math
x=1
y=4
z=3
result = ( (math.fabs((1 / math.tan(x))+6))**(1/3) + math.sqrt(((x+1)**3) / (4*y - 2*z)))
print("result={0:.2f}".format(result))

#3(3)
import math
x=3
y=0.2

result = ( ((5*x*y)/((x**3) -4)) + math.exp(x**2) + math.sqrt( (math.cos(y))**2 - y**2 ))
print("result={0:.2f}".format(result))

#3(4)
import math
x=3
y=5

result = ( math.sqrt(math.fabs(y)) + ((math.atan(math.log(x))**3) / ( (x*y)-y+1) ))
print("result={0:.2f}".format(result))