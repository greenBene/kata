import unittest

def chop_while(target, search_array):

    left_border = 0
    right_border = len(search_array)

    while (left_border < right_border):
        lookup_index = int((left_border + right_border)/2)
        lookup_result = search_array[lookup_index]
        if lookup_result == target:
            return lookup_index

        if lookup_result > target:
            right_border = lookup_index
        else:
            left_border = lookup_index+1

    return -1

def chop_rec(target, search_array):
    return chop_rec_calc(target, search_array, 0, len(search_array))

def chop_rec_calc(target, search_array, left, right):
    if left >= right:
        return -1

    lookup_index = int((left+right)/2)
    lookup_result = search_array[lookup_index]

    if lookup_result == target:
        return lookup_index
    elif lookup_result > target:
        return chop_rec_calc(target, search_array, left, lookup_index)
    else:
         return chop_rec_calc(target, search_array, lookup_index+1, right)
