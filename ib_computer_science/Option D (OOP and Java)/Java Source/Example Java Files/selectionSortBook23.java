public class selectionSortBook23{
	public static void main(String[]args) {
		int elements[] = {1,5,3,86,256,420,9,510,51,24,60};
		int i = 0;
		int temp = 0;
		for (int min = 0; min<10; min++) {
			i=min;
			for(int current =min+1; current<elements.length; current++) {
				if(elements[current]<elements[i]) {
					i=current;
					
				}
			}
		temp=elements[i];
		elements[i]=elements[min];
		elements[min]=temp;
		
		}
		System.out.println("Array after selection sort: ");
		for(int j = 0; j <elements.length; j++) {
			System.out.println(elements[j]+ " ");
		}
	}
}