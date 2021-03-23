public class studentGrades {

	public static void main (String[]args) {
		System.out.println("An array of student grades");

		String [] names = {"Martin", "James" , "Diane"};
		int [] grades = {55, 75, 85};
		int max = grades[0];
		int min=grades[0];
		int  av=0;
		int average=0;
		int m=0;
		String best="0";
		String worst="0";
		for (m=0;m<names.length;m++){
			System.out.println("No" + m+1 + "--Student "+names[m]+"--Mark" + grades[m]);
			
		}
		for (m=0;m<names.length;m++) {
			if (min>=grades[m]) {
				min=grades[m];
				worst=names[m];					
			}
		}
		for (m=0;m<names.length;m++) {
			av=av+grades[m];
			if(max<=grades[m]) {
				max=grades[m];
				best=names[m];
			}
		}
		average=av/10;
		System.out.println("--------");
		System.out.println("Statistics");
		System.out.println("--------");
		System.out.println("minimum mark"+ min + "student" + worst);
		System.out.println("maximum mark"+ max + "Student" + best);
		System.out.println("class average:" + average);
	}
}
