from random import randint

in_file = open("vocabulary.txt", "r")
Eng_list = []
Kor_list = []
for line in in_file:
    Eng_Kor_pair = line.strip().split(": ")
    Eng_list.append(Eng_Kor_pair[0])
    Kor_list.append(Eng_Kor_pair[1])
pair = {}
for i in range(0, len(Kor_list)):
    pair[Kor_list[i]] = Eng_list[i]
while True:
    random_number = randint(0, len(Kor_list) - 1)
    quiz = input(f"{Kor_list[random_number]}: ")
    if quiz == "q":
        break
    if quiz == Eng_list[random_number]:
        print("맞았습니다!\n")
    else:
        print(f"틀렸습니다. 정답은 {Eng_list[random_number]}입니다.\n")
in_file.close()
