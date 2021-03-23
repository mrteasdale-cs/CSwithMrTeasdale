package work;
import javax.swing.JOptionPane;
public class Q5 {
	public static String drawParralellogram(int w, int h, char c) {
		return "";
	}
	public static void drawLeadingSpaces(int h, int l) {
		
	}
	public static void drawFilledLine(int w, char c) {
		
	}
	public static void drawHollowLine(int w, char c) {
		System.out.println();
		for (int i=0;i<(w-2);i++) {
			for (int d=0;d<(w-i-2);d++) {
				System.out.print(" ");
			}
			System.out.print(c);
			for (int p=0;p<(w-2);p++) {
				System.out.print(" ");
			}
			System.out.println(c);
		}

	}
	
	
	public static void main(String[] args) {
		JOptionPane.showMessageDialog(null, "Welcome to Parallelogram-orama");
		String sc = JOptionPane.showInputDialog("Enter character");
		String swid = JOptionPane.showInputDialog("Enter the width");
		String shei = JOptionPane.showInputDialog("Enter the height");
		int wid = Integer.parseInt(swid);
		int hei = Integer.parseInt(shei);
		char[] ac = sc.toCharArray();
		char c = ac[0];
		for (int i=0;i<(hei-1);i++) {
			System.out.print(" ");
		}
		for (int i=0;i<(wid);i++) {
			System.out.print(c);
		}
		System.out.println();
		for (int i=0;i<(hei-2);i++) {
			for (int d=0;d<(hei-i-2);d++) {
				System.out.print(" ");
			}
			System.out.print(c);
			for (int p=0;p<(wid-2);p++) {
				System.out.print(" ");
			}
			System.out.println(c);
		}
		for (int i=0;i<(wid);i++) {
			System.out.print(c);
		}
	}

}
