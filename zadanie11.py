# Write a program that can compute the factorial of given numbers.
# The results should be printed as a comma-separated sequence on a single line.
# Example input: [3, 4, 5]
# Example output: 6, 24, 120

def factorial(number):
    result = 1
    for i in range(1, number + 1):  # Loop starts at 1 and goes up to the number (inclusive)
        result *= i  # Multiply result by the current number
    return result

# Function to compute factorials for a list of numbers
def compute_factorials(numbers):
    results = [factorial(num) for num in numbers]  # Compute factorial for each number in the list
    print(", ".join(map(str, results)))  # Print the results as a comma-separated string

# Example usage
compute_factorials([3, 4, 5])  # Example input
