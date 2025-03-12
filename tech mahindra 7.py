#check whether the multiplication of last 2 elements > multiplication of frst 2 elelments#
a=list(map(int,input().split()))
a.sort()
if a[len(a)-1]*a[len(a)-2] > a[0]*a[1]:
       print(a[len(a)-1]*a[len(a)-2])
else:
      print(a[0]*a[1])
       
  
