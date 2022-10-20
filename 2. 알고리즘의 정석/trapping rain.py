def trapping_rain(buildings):
    total_height = 0
    # 0번과 마지막 인덱스 필요없음
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스에서 양쪽에 가장 높은 건물의 위치를 구함
        max_right = max(buildings[i:])
        max_left = max(buildings[:i])

        # 현재 인덱스에 담길 수 있는 빗물의 높이
        rain_in_index = min(max_left, max_right)

        total_height = total_height + max(0, rain_in_index - buildings[i])
    return total_height


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
