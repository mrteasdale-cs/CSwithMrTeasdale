
public class bubbleSortIB {
    public static void main(String[] args) {  
        int NUMS[] ={15,30,85,25,40,90,50,65,20,60};
        
        System.out.println("Array Before Bubble Sort");  
        for(int C=0; C < 10; C++){
            System.out.print(NUMS[C] + " "); 
	    
        }
        int n=NUMS.length;
        int TEMP=0;
        
	     for(int PASS=0; PASS<9; PASS++){  
	           for(int CURRENT=0; CURRENT <9; CURRENT++){  
	                 if(NUMS[CURRENT]>NUMS[CURRENT+1]){  
	                     TEMP=NUMS[CURRENT]; 
	                     NUMS[CURRENT]=NUMS[CURRENT+1];
	                     NUMS[CURRENT+1]=TEMP;
	                 }
	           }
	     }
	                   	System.out.println();
	  System.out.println("Array After Bubble Sort");  
	  for(int i = 0; i<NUMS.length; i++) {
		  System.out.print(NUMS[i]+ " ");
	             			
	                        			
	                          }
        

        }
}
    
    
