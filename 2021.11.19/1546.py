a = int(input())
sl = list(map(int,input().split()))
mn = max(sl)
pn = 0
for i in range(a):
    sl[i] = sl[i]/mn*100
for i in range(a):
    pn += sl[i]
print(pn/a)
