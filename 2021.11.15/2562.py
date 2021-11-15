Nlist = list(int(input()) for i in range(9))#한꺼번에 입력 받는법
maxN = max(Nlist)
print(maxN)
print(Nlist.index(max(Nlist))+1)
#max함수로 최댓값을 바로찾고, index를 이용해 몇번째인지 바로 찾을수있다.
