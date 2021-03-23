import java.util.Scanner;


public class CaseCalc {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		Scanner kb2 = new Scanner(System.in);
		System.out.print("Please select first operation (ADD, SUB, MLP) > ");
		String selection = kb2.nextLine();
		System.out.print("Please select second operation (ADD, SUB, MLP) > ");
		String selection2 = kb2.nextLine();
		System.out.print("Please enter the first number > ");
		int num1 = kb.nextInt();
		System.out.print("Please enter the second number > ");
		int num2 = kb.nextInt();
		System.out.print("Please enter the third number > ");
		int num3 = kb.nextInt();

		switch (selection) {
		case "ADD":
			switch (selection2) {
			case "ADD":
				System.out.println("("+ num1 + " + " + num2 + ") + " + num3 + " = " + ((num1+num2)+num3));
				break;
			case "MLP":
				System.out.println("("+ num1 + " + " + num2 + ") x " + num3 + " = " + ((num1+num2)*num3));
				break;
			case "SUB":
				System.out.println("("+ num1 + " + " + num2 + ") - " + num3 + " = " + ((num1+num2)-num3));
				break;
			default:
				System.out.println("I do not understand that operation!");
				break;
			}
			break;
		case "MLP":
			switch (selection2) {
			case "ADD":
				System.out.println("("+ num1 + " x " + num2 + ") + " + num3 + " = " + ((num1*num2)+num3));
				break;
			case "MLP":
				System.out.println("("+ num1 + " x " + num2 + ") x " + num3 + " = " + ((num1*num2)*num3));
				break;
			case "SUB":
				System.out.println("("+ num1 + " x " + num2 + ") - " + num3 + " = " + ((num1*num2)-num3));
				break;
			default:
				System.out.println("I do not understand that operation!");
				break;
			}
			break;
		case "SUB":
			switch (selection2) {
			case "ADD":
				System.out.println("("+ num1 + " - " + num2 + ") + " + num3 + " = " + ((num1-num2)+num3));
				break;
			case "MLP":
				System.out.println("("+ num1 + " - " + num2 + ") x " + num3 + " = " + ((num1-num2)*num3));
				break;
			case "SUB":
				System.out.println("("+ num1 + " - " + num2 + ") - " + num3 + " = " + ((num1-num2)-num3));
				break;
			default:
				System.out.println("I do not understand that operation!");
				break;
			}
			break;
		default:
			System.out.println("I do not understand that operation!");
			break;
		}
		
		kb.close();
		kb2.close();
	}

}
