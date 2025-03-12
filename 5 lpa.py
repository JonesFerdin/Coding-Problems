class solution:
 def nextgreatest(self,letters,target):#input
    l=0
    r=len(letters)-1
    while l<=r:
        mid=(l+r)//2
        if letters[mid]>target:
            r=mid-1
        else:
            r=mid+1
    return letters[l%len(letters)]
    return target
ob=solution()
print(ob.nextgreatest(['c','f','j'],'a'))
print(2//2)
