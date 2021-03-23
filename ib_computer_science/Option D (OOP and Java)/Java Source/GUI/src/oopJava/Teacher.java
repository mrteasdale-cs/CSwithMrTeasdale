package oopJava;

public class Teacher extends Person{
	
	private String dept;
	private String classext;
	
	public Teacher(String firstName, String secondName, int personAge, String teacherDept, String classTaught) {
		super(firstName, secondName, personAge);
		dept = teacherDept;
		classext = classTaught;
	}

	public String getDept() {
		return dept;
	}

	public void setDept(String dept) {
		this.dept = dept;
	}

	public String getClassext() {
		return classext;
	}

	public void setClassext(String classext) {
		this.classext = classext;
	}
	
	public String toString() {
		return "\nTeacher Name: "+getfName()+" "+getsName()+"\nAge: "+getAge()+"\nDepartment: "+getDept()+"\nClass Taught: "+getClassext();
	}

}
