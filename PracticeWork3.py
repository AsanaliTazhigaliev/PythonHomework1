a=int(input('First number is: '))
b=int(input('Second number is: '))
c=int(input('Third number is: '))
minimum=0
if a<b and c:
    minimum=a
    if b<a and c:
        minimum=b
        if c<a and b:
            minimum=c
print(minimum, 'is the smallest of three numbers')