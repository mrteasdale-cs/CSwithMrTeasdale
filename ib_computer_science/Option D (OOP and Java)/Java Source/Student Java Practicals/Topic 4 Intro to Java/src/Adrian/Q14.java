// Adrian Pailler; 13/11/20; Wind chill//
package ADRIAN;

import javax.swing.JOptionPane;

public class Q14 {

	public static void main(String[] args) {
		double celcius= Double.parseDouble(JOptionPane.showInputDialog(null,"Enter temperature in Celcius"));
		//parses into double from string in one line//
		double temp = (celcius*1.8)+32;
		if(temp>=10) {
		JOptionPane.showMessageDialog(null,"The wind chill is "+temp+" degrees fahrenheit and is not dangerous or unpleasant");
		//passes through conditions in order until one is met//
		}
		if(temp<10&&temp>=-10) {
			JOptionPane.showMessageDialog(null,"The wind chill is "+temp+" degrees fahrenheit and is unpleasant");
		}
		if(temp<-10&&temp>=-30) {
			JOptionPane.showMessageDialog(null,"The wind chill is "+temp+" degrees fahrenheit and frostbite is possible");
		}
		if(temp<-30&&temp>=-70) {
			JOptionPane.showMessageDialog(null,"The wind chill is "+temp+" degrees fahrenheit and outdoor activities can become dangerous");
		}
		if(temp<-70){
			JOptionPane.showMessageDialog(null,"The wind chill is "+temp+" degrees fahrenheit and will cause frostbite in 30 seconds");
		}
	}

}
