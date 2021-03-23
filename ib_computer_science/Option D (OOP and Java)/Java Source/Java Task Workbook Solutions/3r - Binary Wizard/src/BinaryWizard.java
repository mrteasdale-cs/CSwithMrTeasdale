import java.util.Scanner;


public class BinaryWizard {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
	
		System.out.print("Please enter a number (1-10) > ");
		int num = kb.nextInt();
		
		if (num >= 1 && num <= 10){
			System.out.println("Your binary is: "+Integer.toBinaryString(num));
		} else {
			System.out.println("Number is out of range!");
		}
		
		kb.close();
		
	}

}
