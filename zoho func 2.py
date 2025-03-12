def missing(a):
 a.lower()
 b="qwertyuiopasdfghjklmnbvcxz"
 x=''
 
 for i in b:
    if i not in a:
        x+=i
 return x










a=input()
r=missing(a)
print(r)
