def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]
    # 이미 계산한 값이면 cache에 저장된 값을 리턴
    if count in cache:
        return cache[count]
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(
            profit,
            max_profit_memo(price_list, i, cache)
            + max_profit_memo(price_list, count - i, cache),
        )
        cache[count] = profit
    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
