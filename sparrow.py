import math
a=int(input())
x=a%10
y=(a//10)%10
z=a//100
h=x*x*x+y*y*y+z*z*z
v=math.sqrt(h)
print(h)
print(int(v))
    
