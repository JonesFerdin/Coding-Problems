s=list(map(str,input().split(",")))
l=[]
for i in range(0,len(s)):
    if "a"in s[i] or "e" in s[i] or "i" in s[i] or "o" in s[i] or "u" in s[i]:
        
        l.append("alex")
    else:
        
        l.append("chris")
print(l)
