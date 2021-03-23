package work;
import javax.swing.JOptionPane;
public class Q15 {
	public static Boolean pwcheck(String pw) {
		char[] pwarray = pw.toCharArray();
		int Tcount=0;//the number of large Ts inside the password input
		int tcount=0;//the number of small ts inside the password input
		int ocount=0;
		for(int i=0;i<pw.length();i++)
		{
			if (pwarray[i]=='T') {
				Tcount=Tcount+1;
			}
			if (pwarray[i]=='t') {
				tcount=tcount+1;
			}
			if (pwarray[i]=='o') {
				ocount = ocount+1;
			}
			if (Tcount>=2)
			{
				return true;
			}
			if (tcount>=1 && ocount>=1) {
				return true;
			}
		}
		return false;

	}
	public static void main(String[] args) {
		boolean flag=false;
		while (flag==false) {
		JOptionPane.showMessageDialog(null, "Welcome to password Secure");
		String password = JOptionPane.showInputDialog("Enter password:");
		Boolean goodpassword = pwcheck(password);
		if (password.length()<8) {
			goodpassword=false;
		}
		if (goodpassword==true) {
			JOptionPane.showMessageDialog(null, "Password \""+password+"\" is good");
		}
		else {
			JOptionPane.showMessageDialog(null, "Password \""+password+"\" is bad");
		}
		int dialogbutton=JOptionPane.YES_NO_OPTION;
		int dialogresult = 	JOptionPane.showConfirmDialog(null, "Do you want to play again?","Password Secure",dialogbutton);
		if (dialogresult == 1){
			flag = true;
		}
		}
	}
}
