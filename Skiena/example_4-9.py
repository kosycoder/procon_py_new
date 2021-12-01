def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

def binary_search(array, key):
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = array[middle_index]
        if key < middle_value:
            right_index = middle_index - 1
        elif key > middle_value:
            left_index = middle_index + 1
        else:
            return True
    return False

array = list(map(int, input().split()))
array = quick_sort(array)
print(array)
key = int(input())
print(binary_search(array, key))
