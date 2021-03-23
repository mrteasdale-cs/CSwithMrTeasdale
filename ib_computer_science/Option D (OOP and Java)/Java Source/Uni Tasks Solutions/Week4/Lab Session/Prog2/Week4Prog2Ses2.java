/**********************************************
 **  Java Programming 1                      **
 **  Author     : Myran Teasdale             **         
 **  Student ID : 010125                     **       
 **  Date       : 23/10/08                   **      
 **  Course     : Computer Forensics F2      **    
 **  Description:Calculates the area of a    **   
 **     circle                               **	
 **              							 **       
 **********************************************/


import javax.swing.JOptionPane;

public class Week4Prog2Ses2
{
	
   public static void main(String[] args) 
   {
        double area ;
		final double PI = 3.14159 ;
        String input = JOptionPane.showInputDialog("Enter radius");
        int radius = Integer.parseInt(input);

		if (radius >= 0) 
		{		   
  			area = radius*radius*PI;
  	        JOptionPane.showMessageDialog(null, 
  	        	"The area for the circle of radius " + radius + 
  	        	" is " + area);
		}
		else 
		{
  			JOptionPane.showMessageDialog(null,"Negative radius");
		}
        System.exit(0);
    }
}
