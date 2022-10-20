def select_stops(water_stops, capacity):
    point = 0
    stop_list = []
    for i in range(0, len(water_stops) - 1):
        if water_stops[i] == point + capacity:
            stop_list.append(water_stops[i])
            point = water_stops[i]
        elif (
            water_stops[i] < point + capacity and water_stops[i + 1] > point + capacity
        ):
            stop_list.append(water_stops[i])
            point = water_stops[i]
    stop_list.append(water_stops[-1])
    return stop_list

    # stop_list = []
    # prev_stop = 0
    # for i in range(len(water_stops)):
    #     if water_stops[i] - prev_stop > capacity:
    #         stop_list.append(water_stops[i - 1])
    #         prev_stop = water_stops[i - 1]
    # stop_list.append(water_stops[-1])
    # return stop_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
