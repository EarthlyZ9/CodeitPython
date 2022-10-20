def is_palindrome(word):
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
