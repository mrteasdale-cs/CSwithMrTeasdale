package work;
import javax.swing.JOptionPane;
public class Q1 {
	public static void start(String rohmoohyun) {
		
	}
	public static void main(String[] args) {
		final String TITLE = "The Simple Program";
		start(TITLE);
		String something = JOptionPane.showInputDialog("Enter Something",TITLE);
		JOptionPane.showMessageDialog(null, "You entered "+something);
		
	}

}
