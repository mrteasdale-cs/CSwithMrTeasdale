package oopJava;
import java.util.Scanner;

/* @ userInput.java description...
 * @ author Myran Teasdale
 * @ date 8/3/21
 * @ version 1.0
 */

public class userInput {
	
	
	public static String DataTest(Scanner dataIn) {
	
		try(Scanner sc = new Scanner(System.in)){
		System.out.println("Enter new student course: ");
		String userInput = sc.nextLine();
		return userInput;
		}
		
	}


}
