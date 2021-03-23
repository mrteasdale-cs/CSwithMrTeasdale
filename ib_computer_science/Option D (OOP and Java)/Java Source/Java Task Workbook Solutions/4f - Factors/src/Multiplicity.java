import java.util.Scanner;


public class Multiplicity {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner(System.in);
		
		System.out.print("What is your number? > ");
		int num = kb.nextInt();
		
		System.out.print("The factors of "+num+" are > ");
		for(int i = 1; i <= num; i++){
			if (num%i == 0){
				System.out.print(i + ", ");
			}
		}
		
		kb.close();
		
	}

}
