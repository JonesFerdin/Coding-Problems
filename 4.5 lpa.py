n=int(input())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
m[0][0],m[0][n-1],m[n-1][0],m[n-1][n-1]=m[0][n-1],m[n-1][n-1],m[0][0],m[n-1][0]
for i in m:
    print(*i)
    
