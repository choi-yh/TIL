import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public record Sorting(int[] array) {

    /**
     * {@code O(n^2)} 모든 인덱스를 순회하며 본인의 오른쪽에 있는 값과 비교하여 정렬하는 알고리즘
     */
    public void bubbleSort() {
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] > array[j]) {
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
    }

    /**
     * {@code O(n^2)} 모든 인덱스를 순회하며 본인의 뒤의 인덱스들 중에서 본인보다 작은 최솟값과 위치를 교환하여 정렬하는 알고리즘
     */
    public void selectionSort() {
        for (int i = 0; i < array.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }

            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    public void insertionSort() {
        for (int i = 1; i < array.length; i++) {
            int key = array[i];
            int j;
            for (j = i - 1; j >= 0 && array[j] > key; j--) {
                array[j + 1] = array[j];
            }

            array[j + 1] = key;
        }
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length < 2) {
            return arr;
        }

        int mid = arr.length / 2;
        int[] lower = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] higher = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));

        int[] mergedArr = new int[arr.length];
        int l = 0;
        int h = 0;
        int arrIdx = 0;
        while (l < lower.length && h < higher.length) {
            if (lower[l] < higher[h]) {
                mergedArr[arrIdx] = lower[l];
                l++;
            } else {
                mergedArr[arrIdx] = higher[h];
                h++;
            }
            arrIdx++;
        }

        while (l < lower.length) {
            mergedArr[arrIdx] = lower[l];
            arrIdx++;
            l++;
        }

        while (h < higher.length) {
            mergedArr[arrIdx] = higher[h];
            arrIdx++;
            h++;
        }

        return mergedArr;
    }

    /**
     * {@code O(nlogn)} pivot 을 중심으로 왼쪽은 작은 값들, 오른쪽은 큰값으로 분할 정복하여 정렬하는 알고리즘
     */
    public static int[] quickSort(int[] array) {
        if (array.length <= 1) {
            return array;
        }

        int pivot = array[array.length / 2];
        List<Integer> lower = new ArrayList<>();
        List<Integer> equal = new ArrayList<>();
        List<Integer> higher = new ArrayList<>();
        for (int num : array) {
            if (num < pivot) {
                lower.add(num);
            } else if (num > pivot) {
                higher.add(num);
            } else {
                equal.add(num);
            }
        }

        return IntStream.concat(
                IntStream.of(quickSort(lower.stream().mapToInt(Integer::intValue).toArray())),
                IntStream.concat(
                        IntStream.of(equal.stream().mapToInt(Integer::intValue).toArray()),
                        IntStream.of(quickSort(higher.stream().mapToInt(Integer::intValue).toArray()))
                )
        ).toArray();
    }

    public void quickSortInPlace() {
        sort(0, array.length - 1);
    }

    void sort(int low, int high) {
        if (low >= high) {
            return;
        }

        int mid = partition(low, high);
        sort(low, mid - 1);
        sort(mid, high);
    }

    int partition(int low, int high) {
        int pivot = array[(low + high) / 2];
        while (low <= high) {
            while (array[low] < pivot) {
                low++;
            }
            while (array[high] > pivot) {
                high--;
            }

            if (low <= high) {
                int temp = array[low];
                array[low] = array[high];
                array[high] = temp;

                low++;
                high--;
            }
        }

        return low;
    }

}
