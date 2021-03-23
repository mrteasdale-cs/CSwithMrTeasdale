
public class arrayExample2D {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[][]studentNames=new String[5][2];
		studentNames[0][0]="Mr";
		studentNames[0][1]="Toner";
		studentNames[1][0]="Mrs";
		studentNames[1][1]="Vaughan";
		
		for (int i = 0; i < 5; i++) {
			for (int j=0; j < 5; j++) {
				System.out.println(studentNames[i][j]);
			}
		}
	}

}
