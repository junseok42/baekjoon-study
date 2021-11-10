a = input().split()
hour = int(a[0])
time = int(a[1])
time = time-45
if time < 0 :
  time = 60+time
  hour = hour-1
if hour < 0 :
  hour = 24+hour
print(hour,time)
