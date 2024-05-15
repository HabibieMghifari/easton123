from time import time
x = [int(time()*100)]

a = 3627445327
c = 3284688326
m = (2**64) - 1

def random() -> int:
    x[0] = int((a * x[0] + c) % m)
    return x[0]

def random_range(start: int, end: int) -> int:
    return start + (random() % (end - start + 1))

num = 0
for i in range (10):
    num += random_range(0, 50)
    print(num)
