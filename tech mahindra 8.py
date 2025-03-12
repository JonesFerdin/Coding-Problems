#adding tens place of non same digits and displayingb their sum
a=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
 if (a[i]//10 != a[i]%10):
    c.append(a[i]//10)
print(c)
print(sum(c))
