package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */

public class rootfinder {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String as=JOptionPane.showInputDialog(null, "For the equation ax^2+bc+c enter a");
		String bs=JOptionPane.showInputDialog(null, "For the equation ax^2+bc+c enter b");
		String cs=JOptionPane.showInputDialog(null, "For the equation ax^2+bc+c enter c");
		double a=Double.parseDouble(as);
		double b=Double.parseDouble(bs);
		double c=Double.parseDouble(cs);
		double sqrt=Math.sqrt(b*b-4*a*c);
		double nominator1=sqrt-b;
		double nominator2=-sqrt-b;
		double denominator=2*a;
		
		
		double root1= nominator1/denominator;
		double root2=nominator2/denominator;
		JOptionPane.showMessageDialog(null, "The roots of the equation of "+a+"x^2+"+b+"x+"+c+" are "+root1+"and "+root2);


	}

}
