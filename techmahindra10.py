
a=list(map(int,input().split()))
print(a)
s=0
for i in range(0,len(a)):
 c=0
 for j in range(i+1,len(a)):
     if c<a[i]-a[j]:
        c=a[i]-a[j]
 if s<c:
    s=c        
print(s)
