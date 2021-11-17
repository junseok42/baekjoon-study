nl = list(int(input()) for i in range(10))
for i in range(10):
  nl[i] = nl[i] % 42
nl = set(nl)
print(len(nl))
#set은 중복을 제거해줌 그리고 len으로 중복제거한 리스트의 길이를 측정해주었음
