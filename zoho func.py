
def zoho(a):
    a=list(a)
    c=[]
    for i in a:
     if i.isalpha():
        c.append(i)
    c.sort()
    x=0
    for i in range(0,len(a)):
        if a[i].isalpha():
            a[i]=c[x]
            x+=1
    return ''.join(a)

a=input()
r=zoho(a)
print(r)
