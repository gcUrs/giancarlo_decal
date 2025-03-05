def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result


def temperatureRange(readings):
    return (min(readings), max(readings))


def isWeekend(day):
    return day in [6, 7]


def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)


def decodeNumbers(n):
    last_d = n % 10
    remaining_d = n // 10
    return last_d * (10 ** len(str(remaining_d))) + remaining_d


def find_min_with_for_loop(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def find_max_with_for_loops(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


def find_min_with_while_loop(nums):
    min_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val


def find_max_with_while_loops(nums):
    max_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val


def vowel_and_consonant_count(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0
    for phrase in text:
        if phrase.isalpha():
            if phrase in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)


def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
