import java.util.Scanner;

public class Average {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner kb = new Scanner(System.in);

		boolean boo = true;

		while (boo){
			String arr[] = new String[5];

			for (int i = 0; i <5; i++) {
				System.out.print("Enter word #"+(i+1)+" > ");
				arr[i] = kb.nextLine();
			}

			String longest = arr[0];
			int longestN = 1;
			String shortest = arr[0];
			int shortestN = 1;

			for (int i = 0; i <5; i++){
				if(arr[i].length() > longest.length()){
					longest = arr[i];
					longestN = (i+1);
				}
				if(arr[i].length() < shortest.length()){
					shortest = arr[i];
					shortestN = (i+1);
				}
			}

			System.out.println("Word #"+longestN+" is the largest word: "+longest);	
			System.out.println("Word #"+shortestN+" is the shortest word: "+shortest);	
			System.out.print("\nShall we play this again? (Y/N) > ");
			char answer = kb.nextLine().toUpperCase().charAt(0);
			if (answer == 'N'){
				System.out.println("Ok then, kwaheri!");
				boo = false;
			}
		}
		kb.close();
	}

}
