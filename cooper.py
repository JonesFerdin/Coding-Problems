a=list(map(str,input().split()))
k=input()
s=0
c=''
for i in a:
    if i[0]==k[s]:  
     s+=2
     c="matched"
    else:
     c="not matched"
     break
print(c)
