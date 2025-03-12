#peak value finder#

a=list(map(int,input().split()))
c=[]
for i in range(0,len(a)-1):
    if(a[i-1]<=a[i] and a[i]>=a[i+1]):
       c.append(a[i])
print(c)
c.sort()
print(c[len(c)-1])
