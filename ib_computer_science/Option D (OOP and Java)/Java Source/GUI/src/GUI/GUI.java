package GUI;

import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class GUI {

	public GUI() {


	}

	public static void main(String[] args) {
		JPanel panel = new JPanel();
		JFrame frame = new JFrame();
		frame.setSize(300,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		frame.add(panel);
		
		panel.setLayout(null);
		
		JLabel lblVol = new JLabel("Volume Calculator");
		lblVol.setBounds(100,20,80,25);
		panel.add(lblVol);
		
		
		
		
		
		
		frame.setVisible(true);
		
		
	}

}
