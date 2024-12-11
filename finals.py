"""def factor(n):
    if n%5 == 0:
        f =  n//5
    elif n%4 == 0:
        f =  n//4
    elif n%3 == 0:
        f =  n//3
    elif n%2 == 0:
        f = n//2
    else:
        return n
    return factor(f)

def middle(n):
    if len(n)== 1:
        return n[0]
    if len(n)==2:
        return n[0]+n[1]
    return middle(n[1:-1])

lst = [1,2,4,1,5,6,1,1,4,7,1,9,3]
target = 9


def binary_search(lst, target):
    lst.sort()
    min, max = 0, len(lst)-1
    print(len(lst))
    print(min, max)
    while min <= max:
        mid = (min + max) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            min = mid + 1
        else:
            max = mid - 1

print(binary_search(lst, target))"""


"""def fst_lst(arr, target):
    low, high = 0, len(arr) - 1
    ind = []
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ind.append(mid)
            arr.remove(arr[mid])
        elif arr[mid] < target:
            low = mid + 1
            print("min")
        else:
            high = mid - 1
            print("high")
    for i in range(len(ind)-1):
        if ind[i] == ind[i+1]:
            ind[i+1] += 1
    print(ind)
    return [min(ind), max(ind)] if ind else [-1, -1]

print(fst_lst([1,1,1,1,2,2,3], 1))"""


def bin(arr):
    for i in range(1, len(arr)):
        pass

def selection_sort_limited_swaps(arr, k):
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # If the minimum is not the current element, swap them
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            # Check if we have reached the swap limit
            if swaps >= k:
                return arr

    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
k = 2
sorted_arr = selection_sort_limited_swaps(arr, k)
print("Partially sorted array is:", sorted_arr)
