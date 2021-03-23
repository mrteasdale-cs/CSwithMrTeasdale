import java.util.Scanner;

public class LittleBoxes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);

		boolean boo = true;

		while (boo) {
			char boxes[] = new char[5];

			for (int i = 0; i < 5; i++){
				System.out.print("Please enter character "+(i+1)+" > ");
				boxes[i] = kb.nextLine().charAt(0);
			}
			System.out.print("Here is your output: ");
			for (int i = 0; i < 5; i++){
				System.out.print(boxes[i]);
				if(i != 4){
					System.out.print(" - ");
				}
			}

			System.out.print("\nThat was fun! Would you like to do that again? (Y/N) ");
			char answer = kb.nextLine().toUpperCase().charAt(0);
			if(answer == 'N'){
				boo = false;
			}
		}

		System.out.print("Ok then! Zàijiàn!");
		kb.close();
	}

}
