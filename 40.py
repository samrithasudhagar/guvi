n=int(input())
a=1
b=1
for i in range(0,n):
  if i!=n-1:
    print(a,end=" ")
  else:
    print(a)
  c=a+b
  a=b
  b=c
  
  
