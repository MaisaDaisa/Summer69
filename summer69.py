"""SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14"""

def summer_69(arr):
    if 6 not in arr:
        answer = 0
        for num in arr:
            num += answer
        return answer
    elif 6 in arr:
        answer = 0
        pos6 = arr.index(6)
        pos9 = arr.index(9)
        for num in arr[0: pos6]:
            num += answer
        for num in arr[pos9+1:]:
            num += answer
        return answer


print(summer_69([2, 1, 9, 11]))  # should be 9
print(summer_69([4, 5, 6, 7, 8, 9]))  # should be 9
print(summer_69([1, 3, 5]))  # should be 14
