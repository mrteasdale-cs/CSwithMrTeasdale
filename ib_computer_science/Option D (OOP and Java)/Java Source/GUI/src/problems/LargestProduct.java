package problems;

public class LargestProduct {

	public LargestProduct() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {

		int[][] array2D = new int[5][5];
		
		for(int i=0;i<array2D.length;i++) {
			for(int j=0;j<array2D.length;j++) {	
				int randN = 1+(int)(Math.random()*((9 - 1) + 1));
				array2D[i][j]=randN;
			}
		}
		
		for(int i=0;i<array2D.length;i++) {
			for(int j=0;j<array2D.length;j++) {	
				System.out.print(array2D[i][j]+" ");
			}
			System.out.print("\n");
		}
		
		System.out.println("\nProduct = "+getProduct(array2D));		
		
	}
	static int getProduct(int[][] arr) {
		int prod = arr[0][0];
		int maxProd = 0;
		int tempProd = 0;
		int count = 0;

		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr.length;j++) {	
				

				tempProd=arr[i][j];
				prod+=tempProd;
				count+=1;
						
				if ((prod>maxProd) && (count==2)) {
					maxProd=prod;
					tempProd=0;
					prod=0;
					count=0;
				}
			}
		}
		return maxProd;
	}

}
