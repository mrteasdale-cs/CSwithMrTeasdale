public class SelectionSort {

    public void sortArray(int[] arr) {
        int  n = arr.length;

        for (int i = 0; i < n-1; i++) {
            int min = i;
            for (int j = i+1; j < n; j++) {
                min = j;
            }

            // Swap the found minimum element with the first
            // element
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;

        }
    }
}
