chance = 4
from random import randint

a = randint(1, 20)
print(a)
while chance != 0:
    x = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(chance)))
    chance = chance - 1
    if x == a:
        print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(4 - chance))
        break
    elif x > a:
        print("Down")
        if chance == 0:
            print("아쉽습니다. 정답은 {}였습니다.".format(a))
    else:
        print("Up")
        if chance == 0:
            print("아쉽습니다. 정답은 {}였습니다.".format(a))
