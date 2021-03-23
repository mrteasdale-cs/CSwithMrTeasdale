    import javax.swing.*;


class Week3g
{
  public static void main(String[] args)
  {
    
	String ageString;
	
	ageString = JOptionPane.showInputDialog(
                    null,
                     "Enter age:",
                      "Age",
                    JOptionPane.QUESTION_MESSAGE);
	int age = Integer.parseInt(ageString);
	
	String retire = ""+ (65-age);
	
	
	System.out.println(65-age);
	
	JOptionPane.showMessageDialog( 
     null,  
     retire,  
     "Years Left",    JOptionPane.ERROR_MESSAGE);
     
  }
  
}
