import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class SortingTest {

    private Sorting sorting;

    private final int[] sortedArr = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    @BeforeEach
    public void setUp() {
        int[] arr = {9, 4, 3, 6, 1, 5, 7, 2, 8};
        sorting = new Sorting(arr);
    }

    @Test
    public void bubbleSort() {
        sorting.bubbleSort();
        assertArrayEquals(sortedArr, sorting.array());
    }

    @Test
    public void selectionSort() {
        sorting.selectionSort();
        assertArrayEquals(sortedArr, sorting.array());
    }

    @Test
    public void insertionSort() {
        sorting.insertionSort();
        assertArrayEquals(sortedArr, sorting.array());
    }

    @Test
    public void mergeSort() {
        assertArrayEquals(sortedArr, Sorting.mergeSort(sorting.array()));
    }

    @Test
    public void quickSort() {
        assertArrayEquals(sortedArr, Sorting.quickSort(sorting.array()));
    }

    @Test
    public void quickSortInPlace() {
        sorting.quickSortInPlace();
        assertArrayEquals(sortedArr, sorting.array());
    }
}