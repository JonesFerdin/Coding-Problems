#display max and minimum numbers in a list
a=list(map(int,input().split()))
a.sort()
mx=0
mn=a[0]
for i in range(0,len(a)):
    if i%2==0:
        if mn>a[i]:
            mn=a[i]
    else:
        if mx<a[i]:
            mx=a[i]
print(mx)
print(mn)
print(mx-mn)
    
