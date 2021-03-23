
/**
 * Solution to Mr Singh Car Garage Task
 *
 * @author P Casey
 * @version (a version number or a date)
 */
public class bike extends vehicle
{
    // instance variables - for the vehicle class.
    // variables from the vehicle class are set using the 'super' constructor
    private int wheels;

    /**
     * Constructor for objects of class car, parent variables are set through the super constructor
     */
    public bike(String reg, String make, String model, String colour, String buyer, double price)
    {
        super(reg,make,model,colour,buyer,price);
        this.wheels = 2;
    }

    public double crash()
    {
        taxed = false;
        value = value*0.25;
        return value;
    }
    
    public String getVehicleDetails()
    {
        String output;
        output = super.getVehicleDetails();
        output += "It is a " + wheels + " wheeled bike, perfect for zipping in and out of traffic.";
        return output;
    }
}