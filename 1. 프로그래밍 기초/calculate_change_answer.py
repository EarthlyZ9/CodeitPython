def calculate_change(payment, cost):
    change = payment - cost
    fifty = change // 50000
    ten = (change % 50000) // 10000
    five = (change % 10000) // 5000
    one = (change % 5000) // 1000

    print("50000원 지폐: {}장".format(fifty))
    print("10000원 지폐: {}장".format(ten))
    print("5000원 지폐: {}장".format(five))
    print("1000원 지폐: {}장".format(one))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
