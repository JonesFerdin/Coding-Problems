a=input()
x=[]
y=[]
for i in range(len(a)):
    if a[i]=="(":
      x.append(a[i])
    else:
        y.append(a[i])
print(abs(len(x)-len(y)))

        
     
