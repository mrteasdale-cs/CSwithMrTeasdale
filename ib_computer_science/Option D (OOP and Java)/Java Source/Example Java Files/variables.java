public class rec1

	public static void main (String[]args) {
	public int doSomething(int n)

	{
    	if(n == 0)
      	return 0;
    	else
      	return 1 + doSomething(n - 1);
	}
}