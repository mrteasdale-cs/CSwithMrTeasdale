import java.util.Arrays;

public class MergeSort {

    public static void merge(int[] Left, int[] Right, int[] Arr){

        int Ln = Left.length;
        int Rn = Right.length;
        int i = 0, j = 0, k = 0;

        while ((i < Ln) && (j < Rn)) {
            if (Left[i] <= Right[j]) {
                Arr[k] = Left[i];
                i++;
            } else {
                Arr[k] = Right[j];
                j++;
            }
            k++;
        }

        while (i < Ln) {
            Arr[k] = Left[i];
            i++;
            k++;
        }

        while (j < Rn){
            Arr[k] = Right[j];
            j++;
            k++;
        }

    }

    public void sort(int[] A) {
        int n = A.length;
        if (n <= 1) {
            return; // If the array is of length 1 or empty, it is already sorted.
        }

        int mid = n / 2;
        // one way to copy a range of an array in Java.
        /*int[] left = Arrays.copyOfRange(A, 0, mid);
        int[] right = Arrays.copyOfRange(A, mid, n); */
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        for (int i = 0; i < mid; i++){
            left[i] = A[i];
        }

        for (int i = mid; i < n; i++){
            right[i - mid] = A[i];
        }

        sort(left); // recursive function call
        sort(right); // recursive function call

        merge(left, right, A); // Assuming merge method returns the merged and sorted array.

    }

}
