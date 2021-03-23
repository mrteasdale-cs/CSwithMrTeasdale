package work;
import javax.swing.JOptionPane;
import java.math.*;
public class Q2 {
	public static double power(int power,int exponent){
		double result = Math.pow(power, exponent);
		Math.getExponent(exponent);
		
		return result;
	}
	public static void main(String[] args) {
		String sbass = JOptionPane.showInputDialog("Input the base");
		String sexponent = JOptionPane.showInputDialog("Input the exponent");
		int bass = Integer.parseInt(sbass);
		int exponent = Integer.parseInt(sexponent);
		double result = power(bass,exponent);
		JOptionPane.showMessageDialog(null,"The base "+bass+" to the exponent of "+exponent+" = "+result);
	}

}
