from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    arr = [5, 6, 10, 3, 4, 7]
    sorted_arr = [3, 4, 5, 6, 7, 10]
    print(bubble_sort(arr) == sorted_arr)
