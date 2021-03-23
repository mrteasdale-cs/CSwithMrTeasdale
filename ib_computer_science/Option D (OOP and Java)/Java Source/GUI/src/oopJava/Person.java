package oopJava;

public class Person {
	
	private String fName;
	private String sName;
	private int Age;
	
	public Person(String firstName, String secondName, int personAge) {
		fName=firstName;
		sName=secondName;
		Age=personAge;
	}
	
	public String getfName() {
		return fName;
	}
	public void setfName(String fName) {
		this.fName = fName;
	}
	public String getsName() {
		return sName;
	}
	public void setsName(String sName) {
		this.sName = sName;
	}
	public int getAge() {
		return Age;
	}
	public void setAge(int age) {
		Age = age;
	}

	
}
