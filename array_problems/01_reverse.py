def reverse_array(arr):
    s = 0
    e = len(arr) - 1

    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

    return arr


#  User Input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

result = reverse_array(arr)
print("Reversed Array:", result)
