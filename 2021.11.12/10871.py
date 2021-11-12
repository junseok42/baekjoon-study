a = input().split()
b = input().split()
length = int(a[0])
gap = int(a[1])
for i in b :
  i = int(i)
  if i < gap :
        print(i,end=' ')
