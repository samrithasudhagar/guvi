n=int(input())
s=""
k=[]
for i in range(1,n+1):
        if n%i==0:
            s=s+str(i)+" "
print(s.strip())
