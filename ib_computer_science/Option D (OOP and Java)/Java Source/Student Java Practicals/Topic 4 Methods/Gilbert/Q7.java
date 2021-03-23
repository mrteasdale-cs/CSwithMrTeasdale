package work;
import javax.swing.JOptionPane;
public class Q7 {
	public static int[] readtime(){
		String smin = JOptionPane.showInputDialog("Enter minutes");
		String ssec = JOptionPane.showInputDialog("Enter Seconds");
		int min = Integer.parseInt(smin);
		int sec = Integer.parseInt(ssec);
		int[] myarray = new int[] {min,sec};
		return myarray;
	}
	public static String displaytime(int min, int sec) {
		int dhour = min/60;
		int dmin = min%60;
		String ddmin = (""+dmin);
		if (dmin<10) {
			ddmin = ("0"+dmin);
		}
		String display = (dhour+":"+ddmin+":"+sec);
		return display;
	}
	public static void main(String[] args) {
		int[] record = readtime();
		String display = displaytime(record[0],record[1]);
		JOptionPane.showMessageDialog(null, "Your time was "+display);
	}

}
