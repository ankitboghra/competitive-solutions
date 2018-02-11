S=input()
cnt,max=0,0
for i in S:
  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
    cnt=cnt+1
  else:
    cnt=0
  if(cnt>max):
    max=cnt
print(max)
