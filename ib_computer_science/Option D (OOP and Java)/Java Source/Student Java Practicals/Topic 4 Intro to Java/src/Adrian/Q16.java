// Adrian Pailler; 13/11/20; betting man (die)//
package ADRIAN;
import java.util.*;

import javax.swing.JOptionPane;
public class Q16 {

	public static void main(String[] args) {
		ArrayList<Integer> set = new ArrayList<Integer>();
		for(int i =0;i<3;i++) {
			int role = (int) (Math.random()*(6-1+1)+1);
			set.add(role);
			// generates random numbers and puts them in the set//
	}
		if(set.get(0)==6&&set.get(1)==6&&set.get(2)==6) {
			JOptionPane.showMessageDialog(null,"You roled all 6 and won 20$\n"+set.get(0)+","+set.get(1)+","+set.get(2));
		}
		
		//end of condition one//
		if(set.get(0)==set.get(1) || set.get(0)==set.get(2) || set.get(1)==set.get(2)) {
			if(set.get(0)==set.get(1) || set.get(1)==set.get(2)) {
			JOptionPane.showMessageDialog(null,"You roled two "+set.get(1)+" and won 5$\n"+set.get(0)+","+set.get(1)+","+set.get(2));
		}
			if(set.get(2)==set.get(0)) {
				JOptionPane.showMessageDialog(null,"You roled two "+set.get(2)+" and won 5$\n"+set.get(0)+","+set.get(1)+","+set.get(2));
			}
		}
		// end of condition 2//
		else if(set.get(0)==set.get(1)&&set.get(1)==set.get(2)&&set.get(0)!=6) {
			JOptionPane.showMessageDialog(null,"You roled three "+set.get(0)+" and won 10$\n"+set.get(0)+","+set.get(1)+","+set.get(2));
		}
		//end of condition 3//
		else {
			JOptionPane.showMessageDialog(null,"You lost 1$\n"+set.get(0)+","+set.get(1)+","+set.get(2));
		}
		// end of condition 4//
}
}
