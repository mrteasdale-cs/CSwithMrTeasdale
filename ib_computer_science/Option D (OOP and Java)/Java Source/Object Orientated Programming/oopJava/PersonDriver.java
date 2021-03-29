package oopJava;
import java.util.Scanner;
public class PersonDriver {

	//this is only to run the methods from other java files. Here we create several objects to be able to use the methods in our main method. notice the "extends" keyword. This suggests the PersonDrive class inherits all methods from the Person class/java file
	public static void main(String[] args) {
		boolean addPerson=true;
		// Driver method
		userInput test = new userInput();		
		Scanner dataIn = new Scanner(System.in);
		//Create instances of objects here
		Student newStudent1 = new Student("Joe","Bloggs",18,13,"Computer Science");
		Teacher newTeacher1 = new Teacher("Myran","Teasdale",24,"Engineering and Technology Dept.","13A");
				
		//outputting the information from objects created
		System.out.println(newStudent1);
		System.out.println(newTeacher1);
		
		//testing the changeProgram method from Student class
		String newProgram = newStudent1.changeProgram();
		newStudent1.setProgram(newProgram);
		
		System.out.println("Student changed courses to "+newStudent1.getProgram());
		System.out.println("Updated Student Record\n"+newStudent1.toString()+"\n\n");
		
		//adds new person from user input (student or teacher) - not necessary
		/*while(addPerson==true) {
			
			System.out.println("Would you like to add a new person? \nEnter 1 to continue or 0 to exit");
			try(Scanner sc = new Scanner(System.in)){

			String sc1 = sc.nextLine();
			//int addNew = Integer.parseInt(sc1);
			
			if (sc1.equals("1")) {
				String firstName;
				String secName;
				int sAge;
				System.out.println("Enter students' first name: ");
				firstName = sc.nextLine();
				System.out.println("\nEnter students' surname: ");
				secName = sc.nextLine();
				System.out.println("\nEnter students' age: ");
				sAge = sc.nextInt();
				
				System.out.println("Would you like to add a new teacher or student? \nEnter 1 for Teacher or 2 for Student");
				int tos = sc.nextInt();
				
				if (tos==1) {
					System.out.println("Enter students year: ");
					int year = sc.nextInt();
					System.out.println("\nEnter students program of study: ");
					String program = sc.nextLine();
					Student newStudent2 = new Student(firstName, secName, sAge, year, program);
					System.out.println("New Record Created\n---------------"+newStudent2);
				}
				else if (tos==2) {
					System.out.println("Enter teachers class: ");
					String classExt = sc.nextLine();
					System.out.println("\nEnter teachers department: ");
					String department = sc.nextLine();
					Teacher newTeacher2 = new Teacher(firstName, secName, sAge, classExt, department);
					System.out.println("New Record Created\n---------------"+newTeacher2);
				}
			}
			else {
				addPerson=false;
			}

			}
			
			

						

		}*/

	}

}
