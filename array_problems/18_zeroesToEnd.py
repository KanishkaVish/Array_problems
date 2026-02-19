def move_zeroes(arr):
    result = []

    #add non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)

    # add zeroes
    zero_count = len(arr) - len(result)

    for i in range(zero_count):
        result.append(0)

    return result
