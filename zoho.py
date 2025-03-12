a=str(input())
l=len(a)
for i in range(0,len(a)):
    if(a[i].isnumeric()):
        print(a[i-1]*int (a[i]),end=' ')
