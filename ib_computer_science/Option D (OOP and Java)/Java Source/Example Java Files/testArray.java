
public class testArray { 

	static int binarySearch(String[] A, String itemSought) 
	{ 
		int bottom = 0, top = A.length - 1; 
		while (bottom <= top) { 
			int midpoint = bottom + (top - bottom) / 2; 

			int result = itemSought.compareTo(A[midpoint]); 

			
			if (result == 0) 
				return midpoint; 

		 
			if (result > 0) 
				bottom = midpoint + 1; 

			
			else
				top = midpoint - 1; 
		} 

		return -1; +
	} 


	public static void main(String []args) 
	{ 
		String[] A = {"Anna","Bill","David","Faisal","Jasmine","Jumal","Ken","Mechela"}; 
		String itemSought = "Bill"; 
		int result = binarySearch(A, itemSought); 

		if (result == -1) 
			System.out.println("Element not present"); 
		else
			System.out.println("Element found at "
							+ "index " + result); 
	} 
} 
