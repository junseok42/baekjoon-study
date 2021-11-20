a = int(input())
scl = list(input().split() for i in range(a))
for item in scl:
    Allp = 0
    scount = 0
    for i in item:
        i = int(i)
        Allp += i
    Allp = Allp - int(item[0])
    nanum = Allp/int(item[0])
    for i in item:
        if int(i) > nanum:
            scount += 1
    print("{:.3f}".format(scount/int(item[0])*100)+'%')







    #"{:.3f}".format(a)
    #소수점 반올림
