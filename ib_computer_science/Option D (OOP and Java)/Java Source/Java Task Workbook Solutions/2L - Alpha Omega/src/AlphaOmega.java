import java.util.Scanner;

public class AlphaOmega {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner kb = new Scanner (System.in);
		
		System.out.println("Hi there! Please enter a word with an ODD number of letters:");
		String word = kb.nextLine();
		System.out.println("Please enter a second word with an ODD number of letters:");
		String word2 = kb.nextLine();
		
		int length = word.length();
		int length2 = word2.length();
		
		System.out.println("There are total of "+(length+length2)+" letters in "+word+" and "+word2);
		System.out.println("The first letters are "+word.charAt(0)+" and "+word2.charAt(0));
		System.out.println("The last letters are "+word.charAt(length-1)+" and "+word2.charAt(length2-1));
		System.out.println("The middle letters are "+word.charAt(length/2)+" and "+word2.charAt(length2/2));
		
		kb.close();
	}

}
