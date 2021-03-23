public class Client extends Person {

	private String accountNo;
	private double balance;
	
	Client(String accountNo, String firstName, String lastName, String address, double balance){
		super(firstName, lastName, address);
		this.accountNo = accountNo;
		this.balance = balance;
	}
	
	public String getAccountNo() {
		return accountNo;
	}
	public double getBalance() {
		return balance;
	}
	

	public void setBalanace(double balance) {
		this.balance = balance;
	}
	
	// Abstract method being used here.
	public void setAccountNo(String accountNo) {
		this.accountNo = accountNo;
	}
	
}