import time
print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second

print('start')
time.sleep(10)     # sleep for 10 seconds
print('wake up')