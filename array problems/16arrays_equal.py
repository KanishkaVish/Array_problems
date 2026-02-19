def arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    freq = {}

    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in arr2:
        if num not in freq:
            return False
        freq[num] -= 1
        if freq[num] < 0:
            return False

    return True
