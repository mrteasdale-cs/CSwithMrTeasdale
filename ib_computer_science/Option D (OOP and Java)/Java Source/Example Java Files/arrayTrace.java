
public class arrayTrace {
	public static void main (String[]args) {

int [] array = {3, 8, 2, 5};
int total = 0 ;
for (int i = 1; i < array.length; i++) {
	array[i] = array[i-1];
	total = total + array[i];

	
System.out.println(total);
}
	}
}