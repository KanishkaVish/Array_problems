def rotate_left(arr, k):
    n = len(arr)
    result = []

    k = k % n

    # Add from k to end
    for i in range(k, n):
        result.append(arr[i])

    # Add from start to k-1
    for i in range(k):
        result.append(arr[i])

    return result
