# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_numbers(min_value, max_value, div=5, not_div=7):
    div_number = []
    amount_of_div_nubers = 0


    for i in range(min_value, max_value+1):
        #print(f"number: {i} rest: {i%5}")
        if (i%5 == 0 and i%7!=0):
            div_number.append(i)
            amount_of_div_nubers = amount_of_div_nubers + 1

    return div_number, amount_of_div_nubers

print(find_numbers(5,50))



