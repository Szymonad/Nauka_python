####remove dublicates




def remove_duplicates(lst):

    #first solution
    # lst = sorted(lst)  # Sort the list
    # unique_list = []
    # seen = set()  # Use a set for tracking seen items
    #
    # for item in lst:
    #     if item not in seen:
    #         unique_list.append(item)
    #         seen.add(item)
    #
    # return unique_list

    ###second solution
    unique_list = list(set(lst))
    return unique_list

list1 = [1, 1, 1, 1, 2, 2, 2, 23, 4, 3, 3]
result = remove_duplicates(list1)
print(f"Result: {result}")