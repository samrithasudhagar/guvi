s=input()
l=list(s)
s=""
for i in range(0,len(l)):
    if int(l[i])%2!=0:
        s=s+l[i]+" "
print(s.strip())
