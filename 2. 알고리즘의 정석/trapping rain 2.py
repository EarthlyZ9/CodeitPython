def trapping_rain(buildings):
    total_height = 0
    # 해당 건물 왼쪽에 있는 가장 높은 건물 저장
    left_list = [0] * len(buildings)

    # 해당 건물 오른쪽에 있는 가장 높은 건물 저장
    right_list = [0] * len(buildings)

    # 0번 인덱스는 0번 건물
    left_list[0] = buildings[0]

    # 그 전 인덱스까지 가장 높은 건물이 차례대로 저장되어있기 때문에 left_list[i - 1]만 봐도 됨.
    for i in range(1, len(buildings)):
        left_list[i] = max(left_list[i - 1], buildings[i])

    # 마지막 인덱스는 맨 오른쪽 건물
    right_list[-1] = buildings[-1]
    for i in range(len(buildings) - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # 현재 인덱스에 담길 수 있는 빗물의 높이
    for i in range(len(buildings)):
        rain_in_index = min(left_list[i], right_list[i])

        total_height = total_height + max(0, rain_in_index - buildings[i])
    return total_height


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
