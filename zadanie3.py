# Get a list from the user
user_input = input("Enter a list of integers, separated by commas: ")
nums = list(map(int, user_input.split(',')))

# List operations
first_three = nums[:3]
last_two = nums[-2:]
every_second = nums[::2]
reversed_list = nums[::-1]
sublist = nums[2:6]

# Display results
print(f"1. First 3 elements: {first_three}")
print(f"2. Last 2 elements: {last_two}")
print(f"3. Every second element: {every_second}")
print(f"4. Reversed list: {reversed_list}")
print(f"5. Elements from index 2 to 5: {sublist}")