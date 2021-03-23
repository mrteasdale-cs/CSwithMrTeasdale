
public class instantiating2DArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[][]studentNames=new String[3][2];
		studentNames[0][0]="Mr";
		studentNames[0][1]="Toner";
		studentNames[1][0]="Mrs";
		studentNames[1][1]="Vaughan";
		studentNames[2][0]="Mr";
		studentNames[2][1]="Trett";
		
		System.out.print(studentNames[0][1]+" "+studentNames[1][1]);
		
		String[][]Array= {
				{"Mr","Mrs","Mr"},
				{"Toner","Vaughan","Trett"}};
		
	System.out.print(Array[0][1]+" "+Array[1][1]);
		}
	}


