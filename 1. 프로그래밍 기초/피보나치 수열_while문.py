a = 0
b = 1
temp = 0
count = 0
while count < 20:
    print(b)
    temp = a
    a = b
    b = temp + b
    count = count + 1

# temp가 필요한 이유
# 이전 항을 a, 다음항을 b라고 했을 때, 그 다음 항은 b가 되고 그 다음 다음 항은 a+b가 된다. 즉 a가 b가 되고 b는 a+b가 되는 것.
# a=b라고 지정해버리면 원래의 a가 사라짐. 하지만 b=a+b에서 a는 원래의 a임. a를 저장해둘 임시공간이 필요함. 이게 temp.
