package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 * This program converts Celsisu to Fahrenheit
 */

public class Fahrenheitcelsisu {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String Temperature = JOptionPane.showInputDialog(null, "Enter the tempretaure in celsius");
		int temp = Integer.parseInt(Temperature);
		int Fahrenheit = (int) (temp*1.8+32);
		JOptionPane.showMessageDialog(null, "Temperature in Celsius is "+ temp+" degrees and in fahrenheit "+Fahrenheit+" degrees.");
		

	}

}
