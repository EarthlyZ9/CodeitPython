in_file = open("대치메카 근무시간.txt", "r")
for line in in_file:
    print(line.strip())

# import linecache
# line = linecache.getline('대치메카 근무시간.txt', 2)
# print(line)
# print(type(line))

# in_file = open('대치메카 근무시간.txt', 'r')
# for i in range(1, 2):
#     line = in_file.readline()
# print(line)

# with open('대치메카 근무시간.txt', 'r') as f:
#     print(f.readlines()[1])
