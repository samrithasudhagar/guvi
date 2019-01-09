n,k=map(int,input())
for i in range(n,k):
  s=0
  temp=i
  while temp>0:
    r=temp%10
    s=s+(r*r*r)
    temp=temp//10
    if i==s:
      print(s)n,k=map(int,input())
