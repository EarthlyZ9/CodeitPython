from random import randint


def generate_numbers():
    generated_numbers_list = []
    count = 0
    while count < 6:
        generated_numbers = randint(1, 45)
        if generated_numbers not in generated_numbers_list:
            generated_numbers_list.append(generated_numbers)
            count += 1
    return sorted(generated_numbers_list)


# numbers = generate_numbers()
# print(numbers)


def draw_winning_numbers():
    winning_numbers_list = generate_numbers()
    bonus_number = randint(1, 45)
    while bonus_number in winning_numbers_list:
        bonus_number = randint(1, 45)
    winning_numbers_list.append(bonus_number)
    return winning_numbers_list


# winning_numbers = draw_winning_numbers()
# print(winning_numbers)


def count_matching_numbers(list1, list2):
    match = 0
    for element in list1:
        if element in list2:
            match += 1
    return match


# print(count_matching_numbers(numbers, winning_numbers[:6]))


def check(numbers, winning_numbers):
    winning_numbers_without_bonus = winning_numbers[:6]
    if count_matching_numbers(numbers, winning_numbers_without_bonus) == 6:
        return 1000000000
    elif (
        count_matching_numbers(numbers, winning_numbers_without_bonus) == 5
        and winning_numbers[6] in numbers
    ):
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers_without_bonus) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers_without_bonus) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers_without_bonus) == 3:
        return 5000
    return 0


# print(check(numbers, winning_numbers))
