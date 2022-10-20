# while문
a = 1
while a <= 9:
    b = 1
    while b <= 9:
        print("{} * {} = {}".format(a, b, a * b))
        b += 1
    a += 1

# for문
for a in range(1, 10):
    for b in range(1, 10):
        print(f"{a} * {b} = {a * b}")
