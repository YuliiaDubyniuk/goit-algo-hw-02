from collections import deque


def is_palindrome(phrase: str) -> bool:
    char_list = [char.lower() for char in phrase if char.isalnum()]
    dq = deque(char_list)

    while len(dq) > 1:
        beg_char = dq.popleft()
        end_char = dq.pop()
        if beg_char != end_char:
            return False

    return True


print(is_palindrome("RaceCar12321racecar"))
print(is_palindrome("Hello"))
