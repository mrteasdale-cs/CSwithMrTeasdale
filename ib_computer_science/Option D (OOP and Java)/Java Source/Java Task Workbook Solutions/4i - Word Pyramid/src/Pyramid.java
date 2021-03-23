import java.util.Scanner;


public class Pyramid {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
		
		System.out.print("Please enter a word > ");
		String word = kb.nextLine();
		String pyramid = "";
		
		for (int i=0; i<word.length()-1; i++){
			pyramid = pyramid + word.charAt(i);
			System.out.println(pyramid);
		}
		
		for (int j=0; j<word.length(); j++)
		{
			System.out.println(word.substring(0, word.length()-j));
		}
		
		kb.close();
	}

}
