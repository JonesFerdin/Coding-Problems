n=10
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    c+=a[i]/n
print(int(c))
