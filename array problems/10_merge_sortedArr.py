def merge_sorted(a1, a2):
    i = j = 0
    result = []

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1

    while i < len(a1):
        result.append(a1[i])
        i += 1

    while j < len(a2):
        result.append(a2[j])
        j += 1

    return result
