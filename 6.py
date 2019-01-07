s=int(input())
if s%4==0:
  print("Yes")
elif s%100 and s%400:
  print("Yes")
elif s%100:
  print("No")
elif s%4!=0: 
  print("No")
