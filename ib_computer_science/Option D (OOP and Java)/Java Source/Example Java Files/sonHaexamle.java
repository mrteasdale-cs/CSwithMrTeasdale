import java.util.Arrays;

public class BinarySearch
{
    public static void main(String[] args)
    {
        String[] A = {"Anna","Bill","David","Faisal","Jasmine","Jumal","Ken","Mechela"};
        System.out.println("Please enter name to search for: ");
        Scanner kb = new Scanner(System.in);
        String itemsought = kb.nextLine();
        String newItem=itemsought;
        int searchIndex=binarySearch(A,newItem);
        
        
        int itemFound = 0;
        int searchFailed = 0;
        int top = A.length - 1;
        int bottom = 0;
        int midpoint = 0;
        
        
        
        while ((itemFound == 0) && (searchFailed == 0))
        {
            midpoint = (top + bottom) / 2;
            System.out.println("top, bottom, midpoint: "+top+" "+bottom+" "+midpoint);
            if (A[midpoint] == newItem)
            {
                itemFound = 1;
            }
            if (A[midpoint]<newItem)
            {
            }
            else
            {
                if (bottom > top)
                {
                    searchFailed = 1;
                }
            }
        }
    }
}

