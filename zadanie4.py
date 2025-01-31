def roman_to_int(s):
    roman_to_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    pre_value = 0

    for char in reversed(s):
        cur_value = roman_to_value[char]
        if cur_value < pre_value:
            total -= cur_value
        else:
            total += cur_value
        pre_value = cur_value

    return total

# Example usage
s1 = "IV"
s2 = "XLVIII"
s3 = "MCMXCIV"

print(roman_to_int(s1))  # Output: 3
print(roman_to_int(s2))  # Output: 58
print(roman_to_int(s3))  # Output: 1994
