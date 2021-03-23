
/**
 * Solution to Mr Singh Car Garage Task
 *
 * @author P Casey
 * @version (a version number or a date)
 */
public class vehicle
{
    // instance variables
    public String registration;
    public String make;
    public String model;
    public String colour;
    public String owner;
    public double value;
    public boolean taxed;

    /**
     * Constructor for objects of class vehicle
     * Args used to instantiate variabes
     */
    public vehicle(String reg, String make, String model, String colour, String buyer, double price)
    {
        this.registration = reg;
        this.make = make;
        this.model = model;
        this.colour = colour;
        this.owner = buyer;
        this.value = price;
        this.taxed = true;
    }

    public void sell(String buyer, double price)
    {
        owner = buyer;
        value = price;
    }
    
    public double tax()
    {
        taxed = true;
        value = value*0.9;
        
        return value;
    }
    
    public double crash()
    {
        taxed = false;
        value = value*0.5;
        return value;
    }
    
    public void respray(String newColour)
    {
        colour = newColour;
    }
    
    public String getVehicleDetails()
    {
        String output;
        output = owner + " bought this " + make + ", " + model + " for $" + value + ". ";
        return output;
    }
    
    public String getReg()
    {
        return registration;
    }
    
}
