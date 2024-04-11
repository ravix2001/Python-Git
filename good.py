import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
if(timestamp<12):
    print("Good Morning, Ravi")
else:
    print("Good Evening, Ravi")