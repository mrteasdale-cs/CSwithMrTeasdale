package nicholas1;

import javax.swing.JOptionPane;
/**
 * 
 * @author nicolaspfitzinger
 * @since Nov,11,2020
 */
public class Powers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String ANUM = JOptionPane.showInputDialog(null, "enter a in a^b");
		String BNUM = JOptionPane.showInputDialog(null, "enter b in a^b");
		int a = Integer.parseInt(ANUM);
		int b = Integer.parseInt(BNUM);
		int result=a;
		for(int i=1;i<b;i++) {
			result=a*result;
		}
		System.out.println(a+" to the power of "+b+" is "+result);

	}

}
