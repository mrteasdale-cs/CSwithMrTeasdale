package searchsort;

import java.util.Scanner;

public class Selection_Sort {
	public static void selectionSort(int[] arr) {
		for (int i=0;i<arr.length;i++) {
			int index = i;
			for (int j=(i+1);j<arr.length;j++) {
				if (arr[j]<arr[index]) {
					index = j;//index is the position of the smallest value
				}
			}
			int min=arr[index];
			arr[index]=arr[i];
			arr[i]=min;
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
		System.out.print("Original array: ");
		for (int e=0;e<myarray.length;e++) {
			System.out.print(myarray[e]+" ");
		}
		selectionSort(myarray);
		System.out.println();
		System.out.print("Sorted array: ");

		for (int c=0;c<myarray.length;c++) {
			System.out.print(myarray[c]+" ");
		}
	}

}
