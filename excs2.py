import time

timestamp = (time.strftime('%H:%M:%S'))
print(timestamp)

timestamp = int (time.strftime('%H'))
print(timestamp)

timestamp = int (time.strftime('%M'))
print(timestamp)

timestamp = int (time.strftime('%S'))
print(timestamp)

if (timestamp >= 6 and timestamp < 12):
    print("Good Morning")

elif (timestamp >= 12 and timestamp < 18):
    print("Good Afternoon")
elif (timestamp >= 18 and timestamp < 24):
    print("Good Evening")
elif (timestamp >= 24 and timestamp < 6):
    print("Good Night")
else:
    print("Invalid time")

# https://docs.python.org/3/library/time.html#time.strftime