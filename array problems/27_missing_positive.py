def first_missing_positive(arr):
    n = len(arr)

    for num in range(1, n + 2):   
    # check from 1 upward
        found = False

        for i in range(n):
            if arr[i] == num:
                found = True
                break

        if not found:
            return num
