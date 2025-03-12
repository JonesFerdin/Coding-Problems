a=list(map(str,input().split()))
for i in a:
 e=[]
 s=''
 f=[]
 for a in i:
    if a in 'AEIOUaeiou':
        e.append(a)
    else:
        f.append(a)
 s=''.join(e)
 s+=''.join(f)
 print(s,end=' ')
