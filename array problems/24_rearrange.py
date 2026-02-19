def rearrange_alternate(arr):
    # sort array
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    result = []
    left = 0
    right = n - 1

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])

        left += 1
        right -= 1

    return result
