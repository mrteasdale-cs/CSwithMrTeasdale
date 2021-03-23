import java.util.*;

public class input2DArray {
		public static void main (String[]args) {
			
		
			Scanner input = new Scanner(System.in);
			String[][]Array = new String[3][2];

			for (int i=0; i<4;i++) {
				for (int j=0;j<3; j++) {
		        System.out.println("Please enter Full name and press enter");
		        String row = input.next();
		        String  = input.next();
			
	};
			for (int x=0; x<4;x++) {
				for (int y=0;y<3; y++) {
					System.out.print(Array[x][y] );
					
				}
				System.out.println();
				
				System.out.println(Arrays.deepToString(Array));
				}
			}
	}

}
