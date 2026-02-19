def max_diff(arr):
    n = len(arr)

    if n < 2:
        return 0   

    Mdiff = arr[1] - arr[0]

    for i in range(n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]

            if diff > Mdiff:
                Mdiff = diff

    return Mdiff
