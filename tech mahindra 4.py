
#non duplicate nums
a=list(map(int,input().split()))
a.sort()
c=0
for i in range(0,len(a)):
 if i==0 and  a[i]!=a[i+1]:
     c+=1
 elif i==len(a)-1:
     if a[i]!=a[i-1]:
         c+=1
 else:
    if a[i]!=a[i+1] and a[i]!=a[i-1]:
        c+=1
print(c)
