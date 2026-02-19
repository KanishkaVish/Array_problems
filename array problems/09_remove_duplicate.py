def remove_duplicates(arr):
    result = []
    seen = {}

    for num in arr:
        if num not in seen:
            result.append(num)
            seen[num] = True

    return result
