from itertools import chain

def merge_list(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    print(f"sorted list1: {list1}")
    print(f"sorted list2: {list2}")

    ####first solution
    # new_list = list(chain(list1, list2))
    # new_list = sorted(new_list)
    # return new_list

    ####second solution
    # for item in list2:
    #     list1.append(item)
    # list1 = sorted(list1)
    # return list1

    ####third solution (unpacking)
    combined = [*list1, *list2]
    return combined



list1 = [5, 1, 6]
list2 = [9, 2, 4]
result = merge_list(list1,list2)
print(f"result: {result}")