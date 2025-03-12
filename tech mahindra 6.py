a=list(input())
a.sort()
c=[]
for i in range(0,len(a)):
    if i==0 and a[i]!=a[i+1]:
        c.append(a[i])
    elif i==len(a)-1:
        if a[i]!=a[i-1]:
            c.append(a[i])
    else:
        if a[i]!=a[i+1] and a[i]!=a[i-1]:
            c.append(a[i])
print(c)
