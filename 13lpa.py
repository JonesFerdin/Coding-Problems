
b=3
c=6
l=[]
f=[]
count=1
count2=1
for i in range(b):
    l.append(int(input()))
print(l)
for i in range(c):
    f.append(int(input()))
print(f)

for i in range(0,len(l)-1):
    if l[i]<=b and i==0:
        count+=1
    elif l[i]+l[i+1]<=b:
        count+=1
    else:
        break
print(count)

for i in range(0,len(f)-1):
    if f[i]<=c and i==0:
        count2+=1
    elif f[i]+f[i+1]<=c:
        count2+=1
    else:
        break
print(count2)
        
