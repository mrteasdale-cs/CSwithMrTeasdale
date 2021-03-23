import java.util.Scanner;

public class NumbaGumba {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner (System.in);
		
		System.out.println("Hello there! What is your name?");
		String name = kb.nextLine();
		System.out.println("Hi "+name+ ", what year were you born in?");
		int year = kb.nextInt();
		
		int yearU = (2015 - year)+1;
		int yearD = (2015 - year)-1;
		
		System.out.println("Last year you were "+yearD);
		System.out.println("Next year you will be "+yearU);
		
		
		kb.close();
	}

}
