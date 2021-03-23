import java.io.*;

public class SevenH {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader (new FileReader("7H_Sentencelist.txt"));

		int sentences = 0;
		int words = 0;
		String line;
		
		while ((line = br.readLine()) != null) {

			sentences++;
			
			for (int i = 0; i < line.length(); i++) {
				if(line.charAt(i) == ' ' || line.charAt(i) == '.'){
					words++;
				}
			}
		}
		
		System.out.println("Ok, I count the following...");
		System.out.println("There are "+sentences+" sentences!");
		System.out.println("There are "+words+" words!");
		br.close();
	} 

}
