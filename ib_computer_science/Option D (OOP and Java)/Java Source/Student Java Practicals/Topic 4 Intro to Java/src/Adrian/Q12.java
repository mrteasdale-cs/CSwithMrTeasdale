// Adrian Pailler; 13/11/20; Big Lar//
package ADRIAN;
import javax.swing.*;
public class Q12 {

	public static void main(String[] args) {
	int beep = JOptionPane.showConfirmDialog(null,"Does your computer beep on startup?");
	int disk = JOptionPane.showConfirmDialog(null,"Does your hard drive spin?");
	 if(beep == 0&&disk == 0) {
		JOptionPane.showMessageDialog(null,"Please hold for one of our technicians");
	 }
	if(beep==1&&disk==0) {
		JOptionPane.showMessageDialog(null,"Check the speaker contacts");
	}
	if(beep==0&&disk==1) {
		JOptionPane.showMessageDialog(null,"Check driver contacts");
	}
	if(beep==1&&disk==1) {
		JOptionPane.showMessageDialog(null,"Bring computer in for repair");
	}
	}
}
