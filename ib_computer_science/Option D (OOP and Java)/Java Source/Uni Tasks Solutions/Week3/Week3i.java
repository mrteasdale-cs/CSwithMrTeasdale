/*Java Programming 1
 *
 *
 *Myran Teasdale  010125 Computer Forensics F2
 *Version 1 13/10/08
 */
   
import javax.swing.*;

class Week3i
{
  public static void main(String[] args)
  {
    
    String usrInput;
    
    
	//get part A
	
	usrInput = JOptionPane.showInputDialog(
                    null,
                    "Part A",
                    "Input Results", JOptionPane.QUESTION_MESSAGE);
                    
    int PartA = Integer.parseInt(usrInput);

	//get part B
	
	usrInput = JOptionPane.showInputDialog(
                    null,
                    "Part B",
                    "Input Results", JOptionPane.QUESTION_MESSAGE);
                    
    int PartB = Integer.parseInt(usrInput);
    
	//calculate result
	
	int result = (int)(PartA*0.6) + PartB;
	
	//Display Result
	
	usrInput = JOptionPane.showInputDialog(
                    null,
                    result,
                    "Marks", JOptionPane.QUESTION_MESSAGE);
     
  }
  
}
