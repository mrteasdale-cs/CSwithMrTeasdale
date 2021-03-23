// Adrian Pailler; 12/11/20; Sturgeon heights //
package ADRIAN;
import javax.swing.*;
public class Q10 {

	public static void main(String[] args) {
		JTextField one = new JTextField();
		JTextField two = new JTextField();
		Object [] constants = {
				"Enter the first 3 digit number: ",one,
				"Enter the second 3 digit number: ",two,
		};
		// creates three inputs//
		JOptionPane.showConfirmDialog(null, constants,"Multiplication and division",JOptionPane.INFORMATION_MESSAGE);
		String alpha = one.getText();
		String beta = two.getText();
		 	// changed inputs to variables//
		int second = Integer.parseInt(beta.substring(0));
		int frst = Integer.parseInt(alpha);
			int hundred =Integer.parseInt((beta.substring(0,1)))*100;
			int ten = Integer.parseInt((beta.substring(1,2)))*10;
			int uno = Integer.parseInt((beta.substring(2,3)));
			int ansmult = (frst*hundred)+(frst*ten)+(frst*uno);
			//multiplication//
			// gets the individual sets of hundreds tens and ones//
			int quotient = frst/second;
			int remainder = frst%second;
			int divis = second*quotient;
			//division//
			System.out.println("Multiplication: \n\n \t  "+alpha+"\n\tX "+beta+"\n\t------\n\t"+frst*uno+"\n\t"+frst*ten+"\n\t"+frst*hundred+
					"\n\t------\n\t"+ansmult+"\n\nDivision:\n\n\t     Q: "+quotient+"\n\t     +------\n\t  "+second+" | "+frst+"\n\t        "+divis+"\n\t        ---\n\t      R:"+remainder);
			
		
		

	}

}
