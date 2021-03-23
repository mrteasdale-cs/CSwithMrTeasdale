import java.util.Scanner;

public class PlusMe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
		
		int no1 = (int)(Math.random() * 10 + 1);
		int no2 = (int)(Math.random() * 10 + 1);
		int no3 = (int)(Math.random() * 10 + 1);
		System.out.println("Generating random numbers...");
		//System.out.print("Please enter no 1 > ");
		//int no1 = kb.nextInt();
		//System.out.print("Please enter no 2 > ");
		//int no2 = kb.nextInt();
		//System.out.print("Please enter no 3 > ");
		//int no3 = kb.nextInt();
		
		boolean correct = false;
		
		while (!correct) {
			System.out.print("What is the sum? > ");
			int guess = kb.nextInt();
			if (guess == (no1+no2+no3)){
				System.out.println("Correct! Well done!");
				correct = true;
			} else {
				System.out.println("Sorry, try again!");
			}
			
		}
		kb.close();
		
	}

}
