
int1 = 122


#####first solution
# def palindrone_number(int):
#     string = str(int)
#     reversed_str = string[::-1]
#     print(f"int: {string}, reversed: {reversed_str}")
#     if string == reversed_str:
#         return True
#     else:
#         return False
#

######second solution
def palindrone_number(num):

    string = str(num)
    length_of_string = len(string)
    rev_str = ""

    for i in range(length_of_string):
        rev_str = rev_str + string[length_of_string - 1 - i]

    print(f"int: {string}, reversed: {rev_str}")
    return string == rev_str

result = palindrone_number(int1)
print(result)