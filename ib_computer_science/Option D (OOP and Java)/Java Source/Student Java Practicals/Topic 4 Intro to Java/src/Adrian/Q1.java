// Adrian Pailler; 11/11/20; C-RAP radio//
package ADRIAN;
import javax.swing.JOptionPane;
public class Q1 {

	public static void main(String[] args) {
		String crap = JOptionPane.showInputDialog(null,"Enter temperature in Celcius","input",JOptionPane.QUESTION_MESSAGE);
		//ask for temperature
		double cel = Double.parseDouble(crap);
		double far = (cel*1.8)+32;
		//calculates Fahrenheit
		JOptionPane.showMessageDialog(null,"The temperature in Celcius is: "+cel+" degrees. The temperature in Fharenheit is: "+far+" degrees.","Message",JOptionPane.INFORMATION_MESSAGE);
		// Displays both temps
		JOptionPane.showMessageDialog(null,"Thank you for using C-RAP Radio!","Message",JOptionPane.INFORMATION_MESSAGE);
	}

}
