
public class fillArray {
int main()
{
int array[][]=[5][5];
fillArray(array,5);
printArray(array,5);
return 0;
}
void fillArray(int ar[][5], int numRows) {
	srand(time(0));
	for(int row = 0; row <  numRows; row ++) {
		for (int col = 0; col <5; col++) {
			ar[row][col]=rand() %101;
		}
	}
}
void printArray(const int ar [][5], int numRows) {
	for(int row = 0; row <  numRows; row ++) {
		for (int col = 0; col <5; col++) {
			cout << ar[row][col] << "\t";
		}
		cout << end1;
	}
	
		}
