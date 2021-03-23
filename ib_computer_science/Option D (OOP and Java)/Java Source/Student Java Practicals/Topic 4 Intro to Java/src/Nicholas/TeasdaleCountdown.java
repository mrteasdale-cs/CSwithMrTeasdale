package nicholas1;

import javax.swing.JOptionPane;

public class TeasdaleCountdown {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String countstring = JOptionPane.showInputDialog(null, "Enter a number for the countdown:");
		int countdown=Integer.parseInt(countstring);
		for(int i=countdown;i>0;i=i-1) {
			System.out.println(i+ " students in Teasdale's class,");
			System.out.println(i+ " students in class,");
			System.out.println("He tells a joke, turns his back, ");
			System.out.println(i-1+" students in Teasdale's class!");
			
		}
		
		

	}

}
