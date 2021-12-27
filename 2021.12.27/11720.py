length = int(input())
num = input()
sum = 0
while length > 0 :
    length -= 1
    sum += int(num[length])
print(sum)
