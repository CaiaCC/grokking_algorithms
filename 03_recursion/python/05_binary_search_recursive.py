def binary_search(arr, target):
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)

print("Answer")
print(binary_search([6, 7, 8, 9, 10], 8))
print(binary_search([6, 7, 8, 9, 10], 6))

# Practice
def bs_recursive(arr, target):
    if not arr:
        return -1

    low = 0;
    high = len(arr) - 1
    mid = (low + high) // 2 # //: floor division

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bs_recursive(arr[mid + 1:], target)
    else:
        return bs_recursive(arr[: mid], target)

print("Practice")
print(bs_recursive([6, 7, 8, 9, 10], 8))
print(bs_recursive([6, 7, 8, 9, 10], 6))