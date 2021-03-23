import java.io.*;

public class LetterCount {

	public static void main(String[] args) throws IOException {

		FileReader reader = new FileReader("7B_Batch.txt");
		BufferedReader br = new BufferedReader (reader);

		System.out.println("Counting the As' in the file...");

		int count = 0;
		for (int i = 0; i < 250; i++) {
			if (br.readLine().equalsIgnoreCase("A")) {
				count++;
			}
		}
		System.out.println("I found "+count+" As' in the file!");
		
		br.close();

	} 

}
