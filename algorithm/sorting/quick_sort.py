from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lower, equal, higher = [], [], []
    for num in arr:
        if num < pivot:
            lower.append(num)
        elif num > pivot:
            higher.append(num)
        else:
            equal.append(num)

    return quick_sort(lower) + equal + quick_sort(higher)


def quick_sort_in_place(arr: List[int]) -> List[int]:
    def sort(low, high):
        if low >= high:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1

            while arr[high] > pivot:
                high -= 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1

        return low

    sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    arr = [5, 6, 10, 3, 4, 7]
    sorted_arr = [3, 4, 5, 6, 7, 10]
    print(quick_sort(arr))
    print(quick_sort(arr) == sorted_arr)
    print(quick_sort_in_place(arr))
    print(quick_sort_in_place(arr) == sorted_arr)
