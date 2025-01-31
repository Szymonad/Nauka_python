#
#
# def check(str):
#     valid_char = ('(', ')', '{', '}', '[', ']')
#     pair1 = ('(', ')')
#     pair2 = ('{', '}')
#     pair3 = ('[', ']')
#     bracket_dict = {
#         pair1[0]: pair1[1],
#         pair2[0]: pair2[1],
#         pair3[0]: pair3[1]
#     }
#     for char in str:
#         if char not in valid_char:
#             return "char not in valid_char"
#     if len(str) > 0:
#         for i, char in enumerate(str):
#             if char in bracket_dict:
#                 for x, char2 in enumerate(str):
#                     if char2 in bracket_dict.values():
#                         if char in bracket_dict and bracket_dict[char] == char2:
#                             for index in [i, x]:
#                                 str = str[:index] + str[index + 1:]
#                             return True
#                     else:
#                         return False
#
# str1 = "([])"
# result = check(str1)
# print(result)
#

def check(string):
    valid_char = ('(', ')', '{', '}', '[', ']')
    pair1 = ('(', ')')
    pair2 = ('{', '}')
    pair3 = ('[', ']')
    bracket_dict = {
        pair1[0]: pair1[1],
        pair2[0]: pair2[1],
        pair3[0]: pair3[1]
    }

    # Check if all characters are valid
    for char in string:
        if char not in valid_char:
            return "Invalid character in string"

    stack = []
    for char in string:
        if char in bracket_dict:  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_dict.values():  # If it's a closing bracket
            if stack and bracket_dict[stack[-1]] == char:  # Matching pair
                stack.pop()
            else:
                return False

    # If the stack is empty, all brackets are matched
    return not stack

# Example usage
str1 = "(){}"
result = check(str1)
print(result)

