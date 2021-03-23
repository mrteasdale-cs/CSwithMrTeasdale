 class array {
  
    static int [][] myArray = new int[29][]; 

    public static void main(String[] args) {

    myArray[0] = new int[3];   
    myArray[1] = new int[4];   
    myArray[2] = new int[5];

    for(int i=0; i<20; i++)    
        fillArray(i, i+12);

    System.out.println();
    } 

    private static void fillArray(int row, int col) {

        for( int i=0; i<col; i++)
            myArray[row][i] = i;

        for( int i=0; i<col; i++)
            System.out.print(myArray[row][i]);

        System.out.println();
    }

}
