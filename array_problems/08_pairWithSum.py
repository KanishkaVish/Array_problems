def pair_with_sum(arr, target):
    seen = {}

    for num in arr:
        c = target - num
        if c in seen:
            return (num, c)
        seen[num] = True

    return None
