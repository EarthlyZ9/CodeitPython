out_file = open("vocabulary.txt", "w")
while True:
    Eng = input("영어 단어를 입력하세요: ")
    if Eng == "q":
        break
    Kor = input("한국어 뜻을 입력하세요: ")
    if Kor == "q":
        break
    # out_file.write(f"{Eng}: {Kor}\n")
    out_file.write("%s: %s\n" % (Eng, Kor))
out_file.close()
