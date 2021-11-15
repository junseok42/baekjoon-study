leng = int(input())
nlist = input().split()
maxN = int(nlist[0])
minN = int(nlist[0])
for i in nlist:
  i = int(i)
  if maxN < i :
        maxN = i 
for i in nlist:
  i = int(i)
  if minN > i :
        minN = i
print(minN,maxN)
