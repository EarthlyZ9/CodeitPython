def is_palindrome(word):
    word = list(word)
    original_word = list(word)
    for i in range(round(len(word) / 2)):
        a = word[i]
        word[i] = word[len(word) - 1 - i]
        word[len(word) - 1 - i] = a
    return word == original_word


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
