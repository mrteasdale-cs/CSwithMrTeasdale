import java.util.Scanner;


public class Block {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);
		
		System.out.print("Please enter a number > ");
		int num = kb.nextInt();
		int var = 1;
		
		for (int i=0; i<num; i++){
			for (int j=0; j<var; j++){
				System.out.print("X");
			}
			var++;
			System.out.println("");
		}
		
		kb.close();
		
	}

}
