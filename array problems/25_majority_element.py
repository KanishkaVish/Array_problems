def major_elem(arr):
    n = len(arr)

    for i in range(n):
        count = 0

        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count > n // 2:
            return arr[i]

    return -1
