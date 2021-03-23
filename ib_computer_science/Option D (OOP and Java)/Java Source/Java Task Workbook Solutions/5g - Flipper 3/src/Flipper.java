public class Flipper {

	public static void main(String[] args) {
		// TODO Auto-generated method stu
		
		boolean win = false;
		
		int flip = 0; // Flip number
		int count = 0; // Store up to 3 flips
		int tally = 0; // Store total flips
		
		while(!win){
			tally++;
			flip = (int)(Math.random()*100);
			if (flip <= 50) {
				System.out.println(tally + ": Tails");
				count = 0;
			} else {
				System.out.println(tally + ": Heads");
				count++;
			}
			if (count==3){
				System.out.println("Three in a row! That took "+tally+" flips!");
				win = true;
			}
		}


		
	}

}
