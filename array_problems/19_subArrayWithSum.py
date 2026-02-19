def subarray_with_sum(arr, target):
    n = len(arr)

    for i in range(n):
        current_sum = 0

        for j in range(i, n):
            current_sum += arr[j]

            if current_sum == target:
                return (i, j)

    return -1
