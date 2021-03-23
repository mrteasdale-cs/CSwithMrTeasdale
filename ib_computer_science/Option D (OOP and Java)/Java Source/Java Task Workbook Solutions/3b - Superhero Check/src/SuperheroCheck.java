import java.util.Scanner;

public class SuperheroCheck {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner(System.in);
		
		System.out.println("Please enter your age >");
		int age = kb.nextInt();
		
		if (age > 10){
			System.out.println("You are TOO OLD to be a superhero! :-(");
		} else {
			System.out.println("You can be a superhero! :-)");
		}
		
		kb.close();
	}

}
