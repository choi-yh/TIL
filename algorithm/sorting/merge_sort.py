from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n < 2:
        return arr

    mid = n // 2
    lower = merge_sort(arr[:mid])
    higher = merge_sort(arr[mid:])

    return merge(lower, higher)


def merge(lower: List[int], higher: List[int]) -> List[int]:
    merged_arr = []
    l, h = 0, 0
    while l < len(lower) and h < len(higher):
        if lower[l] < higher[h]:
            merged_arr.append(lower[l])
            l += 1
        else:
            merged_arr.append(higher[h])
            h += 1

    merged_arr += lower[l:]
    merged_arr += higher[h:]

    return merged_arr


if __name__ == "__main__":
    arr = [5, 6, 10, 3, 4, 7]
    sorted_arr = [3, 4, 5, 6, 7, 10]

    print(merge_sort(arr))
    print(merge_sort(arr) == sorted_arr)
