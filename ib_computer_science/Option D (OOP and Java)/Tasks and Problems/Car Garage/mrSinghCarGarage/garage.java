import java.util.ArrayList;
/**
 * Solution to Mr Singh Car Garage Task
 *
 * @author P Casey
 * @version (a version number or a date)
 */
public class garage
{
    // instance variables - replace the example below with your own
    public ArrayList<car> carList= new ArrayList<car>();
    public ArrayList<bike> bikeList = new ArrayList<bike>();
    private int carCount;
    private int bikeCount;

    /**
     * Constructor for objects of class garage
     */
    public garage()
    {
       // ArrayList<car> carList = new ArrayList<car>();
       // ArrayList<bike> bikeList = new ArrayList<bike>();
        carCount=0;
        bikeCount=0;
    }

    public void newCar(String reg, String make, String model, String colour, String buyer, double price, boolean sunroof,int doors, int seats)
    {
        carList.add(new car(reg,make,model,colour,buyer,price,sunroof,doors,seats));
    }
    
    public void newBike(String reg, String make, String model, String colour, String buyer, double price)
    {
        bikeList.add(new bike(reg,make,model,colour,buyer,price));
    }
    
    public void printSales()
    {
        System.out.println("--- Sales List ---");
        for(bike b: bikeList)
        {
            System.out.println(b.getVehicleDetails());
        }
        for(car c: carList)
        {
            System.out.println(c.getVehicleDetails());
        }
    }
}
