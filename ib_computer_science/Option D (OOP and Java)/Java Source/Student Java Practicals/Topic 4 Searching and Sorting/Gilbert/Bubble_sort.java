package searchsort;

import java.util.Scanner;

public class Bubble_sort {
	static void BubbleSort(int[] arr) {
		/**
		 * BubbleSort is a method which performs a bubble sort on a given array.
		 * input :
		 * int[] arr : input array to perform bubble sort on
		 * there is no output in this method, it is an in-place function to perform a bubble sort
		 **/
		int len = arr.length;
		int temp;
		for (int i=0;i<len;i++)
		{
			for (int j = 1; j < (len - i); j++)
			{
				if (arr[j - 1] > arr [j])
				{
					temp = arr [j - 1];
					arr[j - 1] = arr[j];
					arr[j]=temp;
				}
			}
		}
	}

    public static void main(String[] args) {
		Scanner keyboard = (new Scanner(System.in));
		System.out.println("Input the length of the array");
		String slen = keyboard.nextLine();
		int len = Integer.parseInt(slen);
		int[] myarray= new int[len];
		for (int d=0;d<len;d++) {
			System.out.println("Input element of the array");
			String sel = keyboard.nextLine();
			int el = Integer.parseInt(sel);
			myarray[d]=el;
			}
		System.out.print("Origianl array: ");
	    for (int q=0;q<myarray.length;q++){
	    System.out.print(myarray[q]+" ");
	    }
	    BubbleSort(myarray);
	    System.out.println();
		System.out.print("Sorted array: ");
	    for (int q=0;q<myarray.length;q++){
	    System.out.print(myarray[q]+" ");
	    }
    }


}
