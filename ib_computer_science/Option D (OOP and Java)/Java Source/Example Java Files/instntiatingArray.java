import java.util.Arrays;
public class instntiatingArray {

	public static void main (String[]args) {
		String[][]Array = {
				{"Mr","Mrs","Mr"},
			{"Toner","Vaughan","Trett"}
};
		for (int i=0; i<4;i++) {
			for (int j=0;j<3; j++) {
				System.out.print(Array[i][j] );
				
			}
			System.out.println();
			
			System.out.println(Arrays.deepToString(Array));
			}
		}
}
