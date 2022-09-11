import math
x=int(input('x is: '))
t=int(input('t is: '))
z=(9*math.pi*t+10*math.cos(x))*math.pow(math.e,x)/(math.sqrt(t)-math.fabs(math.sin(t)))
print('z will be', z)