package oopJava;
import java.util.*;
public class problem {

	public static void main(String[] args) {

	    Scanner sc = new Scanner(System.in);
	    System.out.println("Plz enter the length of the array");
	    String slen = sc.nextLine();
	    int len = Integer.parseInt(slen);
	    int[] myarray = new int[len];
	    System.out.print("Input elements of the  array: ");
	    for (int i = 0;i<len;i++){
	      String sinput = sc.nextLine();
	      int input = Integer.parseInt(sinput);
	      myarray[i] = input;
	    }
	    boolean bool = bigDiff(myarray);
	    System.out.println(bool);
	}
	
	public static boolean bigDiff(int[] arr){
	    boolean flag=false;

	    for(int i =0; i< arr.length-1; i++){
	      if(((arr[i]==2)&&(arr[i+1]==2)||!(arr[i]==4)&&(arr[i+1]==4))){
	        flag= true;
	      }
	      else {
	      flag= false;
	      }
	    }
	    
	    return flag;
	 }



}

