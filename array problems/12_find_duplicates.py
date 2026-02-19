def find_duplicates(arr):
    seen = {}
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen[num] = True

    return duplicates
