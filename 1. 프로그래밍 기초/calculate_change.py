def calculate_change(payment, cost):
    k = payment - cost
    a = k // 50000
    b = (k - 50000 * a) // 10000
    c = (k - 50000 * a - 10000 * b) // 5000
    d = (k - 50000 * a - 10000 * b - 5000 * c) // 1000
    print("50000원 지폐: " + str(a) + "장")
    print("10000원 지폐: " + str(b) + "장")
    print("5000원 지폐: " + str(c) + "장")
    print("1000원 지폐: " + str(d) + "장")


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
