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
	
	String retirementString = JOptionPane.showInputDialog(
                    null,
                     "Enter the age of Retirement:",
                      "Age",
                    JOptionPane.INFORMATION_MESSAGE);
	int retirement = Integer.parseInt(retirementString);

	System.out.println("Years untill Retirement = " + retirement+ -age);

  }
  
}
