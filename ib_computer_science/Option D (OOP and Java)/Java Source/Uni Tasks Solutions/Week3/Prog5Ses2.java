/* 
 *Prog5Ses2
 *outputs my name plus welcome message
 *Myran Teasdale    
 *1/10/08   
 *Programming 1 Computer Forensics   
 *F2
*/

import javax.swing.*;

class Prog5Ses2
{
  public static void main(String[] args)
  {
 
 String name;
 
	name = JOptionPane.showInputDialog(
                    null,
                    "What is Your Name?",
                    "Input", JOptionPane.QUESTION_MESSAGE);
               
    String hello = ("Hello and Welcome " + name) ;    
                    
  	name = JOptionPane.showInputDialog(null,
                    hello,
                    JOptionPane.INFORMATION_MESSAGE);
                                   
  }
  
}
