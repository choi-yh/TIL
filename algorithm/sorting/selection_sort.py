from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    arr = [5, 6, 10, 3, 4, 7]
    sorted_arr = [3, 4, 5, 6, 7, 10]
    print(selection_sort(arr) == sorted_arr)
