import java.util.Random;

public class BubbleSort {

    /**
     *
     * @param elementsArr - accepts an int array and sorts using the bubble sort method
     */
    void sortArray(int[] elementsArr) {
        int n = elementsArr.length;
        boolean swapped = true;

        while (swapped) {
            swapped = false;
            for (int i = 0; i < n - 1; i++) {

                if (elementsArr[i] > elementsArr[i + 1]) {
                    swapped = true;
                    int temp = elementsArr[i];
                    elementsArr[i] = elementsArr[i + 1];
                    elementsArr[i + 1] = temp;
                }
            }
        }
    }
}
