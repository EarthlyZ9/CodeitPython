def min_coin_count(value, coin_list):
    count = 0
    for coin in sorted(coin_list, reverse=True):
        count = count + (value // coin)
        value = value % coin
    return count


default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
