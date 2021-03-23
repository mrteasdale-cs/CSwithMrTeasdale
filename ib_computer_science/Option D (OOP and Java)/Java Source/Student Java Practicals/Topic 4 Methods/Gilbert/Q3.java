package work;
import javax.swing.JOptionPane;
public class Q3 {
	public static Double VCal(double h, double r) {
		double vol = h*r*r*3.14;
		return vol;
	}

	public static void main(String[] args) {
		boolean flag=false;
		while (flag==false) {
		JOptionPane.showMessageDialog(null, "Welcome to Volume Caulculator");
		String srad = JOptionPane.showInputDialog("Enter radius");
		String shei = JOptionPane.showInputDialog("Enter height");
		double rad = Double.parseDouble(srad);
		double hei = Double.parseDouble(shei);
		double vol = VCal(hei,rad);
		JOptionPane.showMessageDialog(null, "The volume of the cylinder is "+vol);
		int dialogbutton=JOptionPane.YES_NO_OPTION;
		int dialogresult = 	JOptionPane.showConfirmDialog(null, "Do you want to play again?","Password Secure",dialogbutton);
		if (dialogresult == 1){
			flag = true;
		}
		}
		JOptionPane.showMessageDialog(null, "Thank you for playing");
	}

}
