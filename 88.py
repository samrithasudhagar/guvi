def gcd(n,m):
  if m==0:
    return(n)
  else:
    return(gcd(m,n%m))
n,m=map(int,input().split())
p=gcd(n,m)
l=(n*m)//p
print(l)
