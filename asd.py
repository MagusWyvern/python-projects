n = int(input())

n += 1
b = 0

while b != n:
    for x in range(10):
        if x % 2 == 0:
            b = b + x
        else:
            x = -x
            b = b + x
else:
    print(b)
