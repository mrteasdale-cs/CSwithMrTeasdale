public class Average {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr[] = new int[30];

		System.out.println("Generating numbers...");
		
		for (int i = 0; i <30; i++){
			arr[i] = (int)(Math.random() * (75)) + 25;
		}
		
		double total = 0;
		
		for (int i = 0; i <30; i++){
			 total = total + arr[i];
		}
		
		System.out.println("The average number for that series is "+(total/30));	
		
	}

}
