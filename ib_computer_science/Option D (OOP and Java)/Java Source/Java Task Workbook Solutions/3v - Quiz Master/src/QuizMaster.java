import java.util.Scanner;


public class QuizMaster {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		
		int random = (int)(Math.random()*3+1);
		String selection = "";
		
		switch (random) {
			case 1:
				System.out.println("What is the third planet from the sun?");
				System.out.println("a. Mercury");
				System.out.println("b. Venus");
				System.out.println("c. Earth");
				System.out.println("d. Neptune");
				System.out.print("What is your answer? > ");
				selection = kb.nextLine();
				
				selection = selection.toLowerCase();
				
				switch (selection) {
					case "c":
						System.out.println("Correct! Well done! :)");
						break;
					default:
						System.out.println("Wrong answer!!");
						break;
				}
			break;
			case 2:
				System.out.println("Which country has no border with France?");
				System.out.println("a. Germany");
				System.out.println("b. Spain");
				System.out.println("c. Andorra");
				System.out.println("d. Russia");
				System.out.print("What is your answer? > ");
				selection = kb.nextLine();
				
				selection = selection.toLowerCase();
				
				switch (selection) {
					case "d":
						System.out.println("Correct! Well done! :)");
						break;
					default:
						System.out.println("Wrong answer!!");
						break;
				}
			break;
			case 3:
				System.out.println("In what year was DGS founded?");
				System.out.println("a. 1467");
				System.out.println("b. 1576");
				System.out.println("c. 1675");
				System.out.println("d. 1765");
				System.out.print("What is your answer? > ");
				selection = kb.nextLine();
				
				selection = selection.toLowerCase();
				
				switch (selection) {
					case "b":
						System.out.println("Correct! Well done! :)");
						break;
					default:
						System.out.println("Wrong answer!!");
						break;
				}
			break;
		}
		kb.close();
	}

}
