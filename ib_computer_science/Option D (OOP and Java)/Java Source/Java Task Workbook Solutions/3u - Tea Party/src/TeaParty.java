import java.util.Scanner;


public class TeaParty {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		
		System.out.print("Would you like to go to the tea party? (yes/no) > ");
		String selection = kb.nextLine();
		
		selection = selection.toLowerCase();
		
		switch (selection) {
			case "yes":
				System.out.println("Hurray! See you there!");
				break;
			case "no":
				System.out.println("Awww! No fun!");
				break;
			default:
				System.out.println("I don't understand what you are saying...");
				break;
		}
		
		kb.close();
	}

}
