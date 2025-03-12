a=list(map(int,input().split()))
n=int(input())
d=[]
c=0
for i in range(0,len(a)):
    if a[i]%n!=0:
        c+=a[i]
print(c,end=' ')
