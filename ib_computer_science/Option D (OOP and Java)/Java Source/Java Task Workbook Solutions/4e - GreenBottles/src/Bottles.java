import java.util.Scanner;

public class Bottles {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner kb = new Scanner(System.in);
		
		System.out.print("How many bottles are on the wall? > ");
		int num = kb.nextInt();
		
		for(int i = num; i > 0; i--){
			System.out.println(num + " green bottles, hanging on the wall,");
			System.out.println(num + " green bottles, hanging on the wall,");
			System.out.println("and if one green bottle, should accidently fall,");
			
			num = num-1;
			
			System.out.println("there'll be "+num+" green bottles, hanging on the wall!");
			System.out.println("");
		}
		
		kb.close();
		
	}

}
