package oopJava;
import java.util.*;
public class critters {
	//setup instance variables
	private String name;
	private String colour;
	private String specialPower;
	private String eats;
	private String drinks;
	
	//Constructor class to create and manipulate the object
	public critters(String critterName, String favColour, String hasSpecialPower, String itEats, String itDrinks) {
		name = critterName;
		colour = favColour;
		specialPower = hasSpecialPower;
		eats = itEats;
		drinks = itDrinks;
	}
	
	//Instance methods (getters and setters)
	public void setName(String newName) {
		name = newName;
	}
	public void setColour(String newColour) {
		colour = newColour;
	}
	public void setspecialPower(String newPower) {
		specialPower = newPower;
	}
	public void setEats(String newEats) {
		eats = newEats;
	}
	public void setDrinks(String newDrinks) {
		drinks = newDrinks;
	}
	public String getName(String newName) {
		return this.name;
	}
	public String getColour(String newColour) {
		return this.colour;
	}
	//format output of class
	//overriding the toString() method  
	public String toString() {
		return "Your new critter has been created: \nName: "+name+"\nIts favourate colour is "+colour+"\nIts special power is "+specialPower+"\nIt likes to eat "+eats+"\nIt likes to drink "+drinks;
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		//take input from the user
		System.out.println("Enter the details of your new critter\nName:");
		String name = sc.nextLine();
		System.out.println("Favourate Colour: ");
		String colour = sc.nextLine();
		System.out.println("What Power does it have? ");
		String power = sc.nextLine();
		System.out.println("What does it eat? ");
		String eats = sc.nextLine();
		System.out.println("What does it drink? ");
		String drinks = sc.nextLine();
		sc.close();
		
		//create new object/instance of critters using the variables above
		critters myCritter = new critters(name, colour, power, eats, drinks);
		//create a new critter object using static strings
		critters myOtherCritter = new critters("Bill","Violet","Invisibility","Garbage","Crude Oil");
		
		//output the results
		System.out.println(myCritter.toString());
		//output other critter
		System.out.println(myOtherCritter.toString());
		
		//set a new critter name of bob
		myCritter.setName("Bob");
		System.out.println(myCritter.getName("Bob"));
		
	}
}
