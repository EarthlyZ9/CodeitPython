def flip(some_list):
    if len(some_list) <= 1:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# base case의 시간복잡도 O(1)
# some_list[-1:]의 시간복잡도 O(1)
# some_list[:-1]의 시가복잡도 O(n-1)
# 재귀적 부분 제외 시간복잡도는 총 O(n)
# 재귀적 부분 시간복잡도: 리스트 길이가 n, n번 호출되므로 O(n)
# 총 시간복잡도 O(n^2)
