def all_subarrays(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i, n):
            sub = []
            for k in range(i, j + 1):
                sub.append(arr[k])
            result.append(sub)

    return result
