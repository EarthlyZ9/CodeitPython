in_file = open("vocabulary.txt", "r")
for line in in_file:
    Eng_Kor_pair = line.strip().split(": ")
    quiz = input("%s: " % (Eng_Kor_pair[1]))
    if quiz == Eng_Kor_pair[0]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(Eng_Kor_pair[0]))
in_file.close()
