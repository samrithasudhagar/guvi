s=int(input())
if s%400==0 or (s%4==0 and s%100!=0):
  print("Yes")
else:
  print("no")
