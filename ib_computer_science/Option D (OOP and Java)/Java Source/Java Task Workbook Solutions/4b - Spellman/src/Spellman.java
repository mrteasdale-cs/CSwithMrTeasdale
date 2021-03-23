import java.util.Scanner;


public class Spellman {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner(System.in);
		
		System.out.print("Please enter your 7 letter word > ");
		String word = kb.nextLine();
		
		String temp = "";
		
		for (int i = 0; i < 7; i++){
			temp = temp + word.charAt(i);
			System.out.println(temp);
		}
		
		kb.close();
		
	}

}
