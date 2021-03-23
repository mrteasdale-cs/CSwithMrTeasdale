
/**
 * Solution to Mr Singh Car Garage Task
 *
 * @author P Casey
 * @version (a version number or a date)
 */
public class car extends vehicle
{
    // instance variables - for the car class.
    // variables from the vehicle class are set using the 'super' constructor
    private int wheels;
    private boolean sunroof;
    private int doors;
    private int seats;

    /**
     * Constructor for objects of class car, parent variables are set through the super constructor
     */
    public car(String reg, String make, String model, String colour, String buyer, double price, boolean sunroof,int doors, int seats)
    {
        super(reg,make,model,colour,buyer,price);
        this.wheels = 4;
        this.sunroof = sunroof;
        this.doors = doors;
        this.seats = seats;
    }
    
    public String getVehicleDetails()
    {
        String output;
        output = super.getVehicleDetails();
        output += "It has " + doors + " doors, and " + seats + " seats.";
        return output;
    }
}
