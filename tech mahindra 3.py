import math
s=list(map(int,input().split()))
a=int(input())
c=0
for i in range(a,len(s)):
  c+=abs(s[i]-s[i-1])
print(c)
    
