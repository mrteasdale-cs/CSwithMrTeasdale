import java.util.Scanner;


public class Selector {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner(System.in);
		
		System.out.println("How many characters do you need to store?");
		int num = kb.nextInt();
		
		if (num < 129){
			System.out.println("I would recommend you use Basic ASCII.");
		} else if (num < 257) {
			System.out.println("I would recommend you use Extended ASCII.");
		} else {
			System.out.println("I would recommend you use Unicode.");
		}
		
		kb.close();
		
	}

}
