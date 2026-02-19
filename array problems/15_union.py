def union(arr1, arr2):
    result = []
    seen = {}

    for num in arr1:
        if num not in seen:
            result.append(num)
            seen[num] = True

    for num in arr2:
        if num not in seen:
            result.append(num)
            seen[num] = True

    return result
