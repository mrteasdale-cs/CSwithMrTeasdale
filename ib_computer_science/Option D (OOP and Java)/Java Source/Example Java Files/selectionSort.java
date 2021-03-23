
public class selectionSort {
public static void main (String[]args) {
	int arr[] = {4,2,7,5,3,9,12};
	
	 System.out.println("Array Before Bubble Sort");  
     for(int C=0; C < 10; C++){
         System.out.print(arr[C] + " "); 
     }

	int numitems=arr.length;
	int Temp=0;
	for(int i=0; i<numitems; i++) {
		for (int j=i+1; i<numitems;i++) {
			if (arr[i]<arr[j]) {
				Temp=arr[i];
				arr[i]=arr[j];						
				arr[j]=Temp;
			}
			}
	     System.out.println();
				
			}

	 System.out.println("After Selection Sort");  
     for(int i:arr){  
         System.out.print(i+" "); 
			}
	}
	
}

