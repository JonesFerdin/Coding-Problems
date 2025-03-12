a=int(input())
b=int(input())
e=a//10
f=b//10
x=e%10
print(x)
y=f%10
print(y)
c= list(str(a))
d=list(str(b))
print(c)
print(d)
h=[]
g=[]

for i in range(0,len(c)):
    if i==1:
        h.append(str(y))
    else:
        h.append(c[i])
for i in range(0,len(d)):
    if i==1:
       g.append(str(x))
    else:
        g.append(d[i])
s=''
s1=' '
for i in h:
    s+=i
for i in g:
    s1+=i
print(int(s))
print(int(s1))
    
        
