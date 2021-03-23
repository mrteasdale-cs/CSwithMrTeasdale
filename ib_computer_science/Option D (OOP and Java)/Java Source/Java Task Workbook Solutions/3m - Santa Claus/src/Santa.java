import java.util.Scanner;


public class Santa {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
		
		System.out.println("Have you been good this year? (yes/no) > ");
		String good = kb.nextLine();
		System.out.println("Have you been naughty or nice? (naughty/nice) > ");
		String n = kb.nextLine();
		
		if (good.equals("yes") && n.equals("nice")) {
			System.out.println("You will get presents this year!");
		} else if (good.equals("no") && n.equals("naughty")) {
			System.out.println("You will get a lump of coal!");
		} else {
			System.out.println("You will have to wait and see!");
		}
		
		kb.close();
	}

}
