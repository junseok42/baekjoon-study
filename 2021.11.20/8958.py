a = int(input())
ql = list(input() for i in range(a))
for item in ql:
    stack = 0
    score = 0
    for ox in item:
        if ox == 'O' :
            score = score + stack + 1
            stack += 1
        else :
            stack = 0
    print(score)    
