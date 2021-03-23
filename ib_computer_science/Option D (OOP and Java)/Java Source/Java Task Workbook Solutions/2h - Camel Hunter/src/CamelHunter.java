import java.util.Scanner;

public class CamelHunter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner kb = new Scanner (System.in);
		
		System.out.println("Hi there! Please enter a 10 letter word");
		String word = kb.nextLine();
		
		System.out.println("Camelising this word...");
		
		String uc = word.toUpperCase();
		String lc = word.toLowerCase();
		
		System.out.print(uc.charAt(0));
		System.out.print(lc.charAt(1));
		System.out.print(uc.charAt(2));
		System.out.print(lc.charAt(3));
		System.out.print(uc.charAt(4));
		System.out.print(lc.charAt(5));
		System.out.print(uc.charAt(6));
		System.out.print(lc.charAt(7));
		System.out.print(uc.charAt(8));
		System.out.print(lc.charAt(9));
		
		kb.close();
	}

}
