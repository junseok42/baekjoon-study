a = int(input())
for i in range(a):
  b,c = map(int,input().split())
  print(b+c)
  
map => split으로 쪼개준 b와 c를 int로 변환해 값을 정해줌. 지정해주는 변수가 하나일시 새로운 리스트를 생성함. 
