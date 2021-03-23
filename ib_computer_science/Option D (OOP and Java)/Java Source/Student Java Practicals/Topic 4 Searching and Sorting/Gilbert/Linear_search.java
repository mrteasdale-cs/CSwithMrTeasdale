package searchsort;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Linear_search {
    public static int mymethod(int arr[], int x)
    /**
     * setting up a method mymethod containing linear search adopting for loop
     * input : 
     * int arr[] : array that the list will search
     * int x : item being searched in the array
     * output : 
     * return i : outputs the index of the item being search
     * return -1 : when the item is not found
     **/
    { 
        int n = arr.length; 
        for (int i = 0; i < n; i++)  
        { 
            if (arr[i] == x) 
                return i; 
        } 
        return -1; 
    } 
    
	public static void main (String[] args) {
		String slen = JOptionPane.showInputDialog("Input Length of the array");
		int len = Integer.parseInt(slen);
		int[] arr= new int[len];
		for (int d=0;d<len;d++) {
			String sel = JOptionPane.showInputDialog("Input element of the array");
			int el = Integer.parseInt(sel);
			arr[d]=el;
		}
		String ssearch = JOptionPane.showInputDialog("Please input item you wish to search");
        int search = Integer.parseInt(ssearch);
        int result = mymethod(arr, search); 
        if (result == -1) {
            JOptionPane.showMessageDialog(null, "Element is not present in array"); 
        }
        else {
        	String full = "";
        	for (int i=0;i<len;i++) {
        		full = full + arr[i]+" ";
        	}
            JOptionPane.showMessageDialog(null, "In array " + full + ", Element "+ search + " is present at index "+ result);
        }
	}
}