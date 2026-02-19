def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    result = [0] * n

    for i in range(n):
        result[(i + k) % n] = arr[i]

    return result
