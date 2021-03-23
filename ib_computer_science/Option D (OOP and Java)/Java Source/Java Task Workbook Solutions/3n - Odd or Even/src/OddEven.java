import java.util.Scanner;


public class OddEven {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
		
		System.out.print("Please enter a number between 1 and 100 > ");
		int num = kb.nextInt();
		
		if (num >= 1 && num <= 100){
			if (num % 2 == 0){
				System.out.println("Number is EVEN!");
			} else {
				System.out.println("Number is ODD!");
			}
		} else {
			System.out.println("Number is not between 1 and 100!");
		}
		
		kb.close();
	}

}
