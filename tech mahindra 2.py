a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    if a[i]<14:
        c+=a[i]
        
print(c)


