# import time
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)

# timestamp = time.strftime("%H")
# print(timestamp)

# timestamp = time.strftime("%M")
# print(timestamp)

# timestamp = time.strftime("%S")
# print(timestamp)

# Good Morning: 00.01 to 11.59.
# Good Afternoon: 12.01 to around 16.00.
# Good Evening: 16.00 to 23.59.

import time 

current_time = time.strftime('%H:%M:%S')
print(current_time)
hour = int(time.strftime('%H'))
minuts = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

if hour>=0 and hour<=11 and minuts>=0 and minuts<=59:
    print("Good Morning!")
elif hour>=12 and hour<=16 and minuts>=1 and minuts<=60:
    print("Good Afternoon")
else:
    print("Good Evening!")


