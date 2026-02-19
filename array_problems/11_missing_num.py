def missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in arr:
        actual_sum += num

    return expected_sum - actual_sum
