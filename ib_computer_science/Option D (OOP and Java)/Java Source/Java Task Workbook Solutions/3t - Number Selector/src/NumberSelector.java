import java.util.Scanner;


public class NumberSelector {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		
		System.out.print("Please enter either 1, 2 or 3 > ");
		int selection = kb.nextInt();
		
		switch (selection) {
			case 1:
				System.out.println("You entered ONE!");
				break;
			case 2:
				System.out.println("You entered TWO!");
				break;
			case 3:
				System.out.println("You entered THREE!");
				break;
			default:
				System.out.println("You did not enter a valid number!");
				break;
		}
		
		kb.close();
	}

}
