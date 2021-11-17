a,b,c = [int(input()) for i in range(3)]
N = str(a*b*c)
for i in range(10):
    print(N.count(str(i)))
#count함수는 문자열에서 그 문자가 몇개있는지 세주는 함수임
