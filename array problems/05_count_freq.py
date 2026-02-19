def frequency(arr):
    freq = {}

    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq
