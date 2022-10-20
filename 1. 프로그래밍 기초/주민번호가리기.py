def mask_security_number(security_number):
    security_number = list(security_number)
    for a in range(len(security_number) - 4, len(security_number)):
        security_number[a] = str("*")
    security_number_str = ""
    for i in security_number:
        security_number_str = security_number_str + str(i)
    return security_number_str


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
