import java.util.Stack;

public class intarraystack {
public static void main (String[]args) {
	int [] Line = {1,4,7,9,5};
	Stack S = new Stack();
	int counter = 0;
	for(counter = 0; counter<Line.length;counter++) {
		S.push(Line[counter]);
	}
	System.out.println(S);
}
}
