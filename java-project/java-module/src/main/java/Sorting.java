import java.util.Arrays;

public class Sorting {

    private final int[] array;

    public Sorting(int[] array) {
        this.array = array;
    }

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

    public int[] getArray() {
        return array;
    }

}
