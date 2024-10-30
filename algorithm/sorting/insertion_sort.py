from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    arr = [5, 6, 10, 3, 4, 7]
    sorted_arr = [3, 4, 5, 6, 7, 10]
    print(insertion_sort(arr))
    print(insertion_sort(arr) == sorted_arr)
