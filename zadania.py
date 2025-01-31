def two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
        print(num_to_index)


# Example usage
nums = [2, 3, 4, 5, 11, 15]
target = 20
result = two_sum(nums, target)
print(result)
