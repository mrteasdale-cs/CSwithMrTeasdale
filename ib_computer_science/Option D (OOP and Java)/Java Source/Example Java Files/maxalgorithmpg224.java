
public class maxalgorithmpg224 {
public static void main (String[]args) {
	int max=10;
	int sum=0;
	int count=0;
	
	for(count=0;count<max-4;count++) {
		System.out.println(count);
		sum=max-4;
		count=max-3;
		System.out.println("count is:" +count);
		
		for(sum=3;sum<5;sum++) {
			System.out.println(count);
			if(count==0 && max>0){
				
				System.out.println("Hello");
			}
			else if (count<4) {
				System.out.println("Go for it");
				
			}
			else {
					System.out.println("OK");
				}
				
			}
		System.out.println("count is +"+count);
		}
	System.out.println("count+"+count);
	sum=sum+count;
	
	System.out.println("Total = "+sum);
	System.out.println("Max = "+count);
	
	}
}

