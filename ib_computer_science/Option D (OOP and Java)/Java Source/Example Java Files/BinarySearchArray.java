import java.util.*;
	public class BinarySearchArray {
	public static void main(String[]args) {
			String [] A = {"Anna","Bill","David","Faisal","Jasmine","Jumal","Ken","Michela","Pavel","Rosa","Stepan","Tom","Zac"};
			System.out.println("Please enter name to search for: ");
			Scanner kb = new Scanner (System.in);
			String itemsought = kb.nextLine();
			int itemFound = 0;
			int searchFailed = 0;
			int top = A.length-1;
			int bottom = 0;

			while (! itemFound) & (! searchFailed){
				
			    midpoint = int((top + bottom)/2)
			    print("top, bottom, midpoint", top, bottom, midpoint)
			    if A[midpoint]==itemSought:
			        itemFound = 1
			    else:
			        if bottom > top:
			            searchFailed = 1
			        else:
			            if A[midpoint]<itemSought:
			                bottom = midpoint + 1      
			            else:
			                top = midpoint - 1

			#endwhile
			if itemFound:
			    print("item is at position ",midpoint)
			else:
			    print ("item is not in the array")
	}
}
