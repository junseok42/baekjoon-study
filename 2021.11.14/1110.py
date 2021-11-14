a = int(input())
temp = a
count = 0
while True :
  first = temp // 10 
  sec = temp % 10
  add = (first + sec) % 10
  temp = sec * 10 + add
  count += 1
  if temp == a :
    print(count)
    break
    
    
    
#문자열 인덱스를 이용해 하려했으나 잘못된것을 알고 구글링을 통해 나눗셈을 통한 풀이가 더욱더 명확하다는 것을 알고 적용함.
#참고// 나머지(%)=> 나머지만 취득, 버림(//)=> 몪만 취득 이용해서 풀었음.
