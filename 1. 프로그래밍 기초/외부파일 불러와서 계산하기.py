in_file = open("대치메카 근무시간.txt", "r")
line_list = []
for line in in_file:
    one_line_list = line.split()
    line_list.append(one_line_list[1])
# print(line_list)
sum = 0
for i in line_list:
    sum = sum + int(i)
# print(sum)
print(sum / len(line_list))

# in_file = open('대치메카 근무시간.txt', 'r')
# sum = 0
# line_count = 0
# for line in in_file:
#     data = line.strip().split(": ")
#     amount = int(data[1])
#     sum = sum + amount
#     line_count += 1
# print(sum / line_count)
