    import javax.swing.*;


class Week3g
{
  public static void main(String[] args)
  {
    
	String ageString = JOptionPane.showInputDialog(
                    null,
                     "Enter age:",
                      "Age",
                    JOptionPane.INFORMATION_MESSAGE);
	int age = Integer.parseInt(ageString);
	
	System.out.println(65-age);

  }
  
}
