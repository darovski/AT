def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b

def rest(a, b):
    if b == 0:
        raise ValueError('Деление на ноль невозможно')
    return a % b

def count_vowels(s):
    vowels = "aeiouAEIOUАаеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Строка, содержащая все гласные
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count