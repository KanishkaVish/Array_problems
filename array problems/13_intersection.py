def intersection(arr1, arr2):
    result = []
    seen = {}

    for num in arr1:
        seen[num] = True

    for num in arr2:
        if num in seen:
            result.append(num)

    return result
