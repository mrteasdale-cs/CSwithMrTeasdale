package nicholas1;

import javax.swing.JOptionPane;

public class Fibronacci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String Counter = JOptionPane.showInputDialog(null, "How many numbers do you want to display");
		int count=Integer.parseInt(Counter);
		int num1 = 0, num2 = 1;
        System.out.print("Fibonacci Series of "+count+" numbers:");

        for (int i = 1; i <= count; ++i){
            System.out.print(num1+" ");
            int sumOfPrevTwo = num1 + num2;
            num1 = num2;
            num2 = sumOfPrevTwo;
        }
	}
}

