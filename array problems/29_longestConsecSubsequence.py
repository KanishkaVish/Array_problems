def longest_consecutive(arr):
    n = len(arr)

    # sort
   
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    longest = 1
    curr = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1] + 1:
            curr += 1
        elif arr[i] != arr[i - 1]:
            curr = 1

        if curr > longest:
            longest = curr

    return longest
