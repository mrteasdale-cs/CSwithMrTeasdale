package oopJava;
import java.util.*;
public class Student extends Person{

	private int Grade;
	private String program;

	public Student(String firstName, String secondName, int personAge, int studentGrade, String studentProgram) {
		super(firstName, secondName, personAge);
		Grade = studentGrade;
		program = studentProgram;
	}

	//Getter and Setter Methods (do not worry about these just yet)
	public int getGrade() {
		return Grade;
	}
	public void setGrade(int grade) {
		Grade = grade;
	}
	public String getProgram() {
		return program;
	}
	public void setProgram(String program) {
		this.program = program;
	}
	
	// Change Program method to allow the program to change the students' course
	public String changeProgram() {
		try(Scanner sc = new Scanner(System.in)){
		System.out.println("Enter new student course: ");
		String newProgram = sc.nextLine();
		return newProgram;
		}
	}
	
	public String toString() {
		return "\nStudent Name: "+getfName()+" "+getsName()+"\nAge: "+getAge()+"\nCourse: "+getProgram()+"\nYear: "+getGrade();
	}	
	
}
