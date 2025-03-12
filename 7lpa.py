a=list(str(input()))
b=[]
for i in range(len(a)-1,-1,-1):
 if a[i].isalpha():
     b.append(a[i])
y=0
for i in range(0,len(a),1):
    if a[i].isalpha():
        a[i]=b[y]
        y+=1
for i in a:print(i,end=" ")
 
    


