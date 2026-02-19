def max_prod_pair(arr):
    n = len(arr)
    max_prod = arr[0] *arr[1]
    pair = (arr[0],arr[1])

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]

            if product > max_prod:
                max_prod = product
                pair =(arr[i], arr[j])

    return pair
