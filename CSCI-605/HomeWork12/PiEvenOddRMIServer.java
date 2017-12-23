package HomeWork12;
/*
 *  PiEvenOddRMIServer.java
 * 
 *  Version: PiEvenOddRMIServer.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * This program calculates the number of Even-Odd values of Pi using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class PiEvenOddRMIServer extends UnicastRemoteObject implements PiEvenOddRMIInterface {
	private static final long serialVersionUID = 1L;
	private static long evenCounter = 0;
	private static long oddCounter = 0;

	protected PiEvenOddRMIServer() throws RemoteException {
		super();
	}
	
	/**
	 *  To return odd count value
	 * 
	 * @return		odd count 
	 */
	public long getOddCount() throws RemoteException { 
		return oddCounter;
	}
	
	/**
	 *  To return even count value
	 * 
	 * @return		even count
	 */
	public long getEvenCount() throws RemoteException { 
		return evenCounter;
	}

	/**
	 *  To open communication and start the execution
	 * 
	 * @return		no return value
	 */
	@Override
	public void calculateEvenOddPiValues(char[] contentsOfFile) throws RemoteException {
		PiEvenOddRMIServer evenOddRMIServer = new PiEvenOddRMIServer();
		//For the character array calculate the number of even and odd values 
		for( int i = 0; i < contentsOfFile.length; i++) {
			evenOddRMIServer.countEvenOdd( contentsOfFile[i] );
		}
	}
	
	/**
	 *  Calculates whether a character is an even or odd digit
	 * 
	 * @param	character	Checks whether this character is even or odd
	 * 
	 * @return				no return value
	 */
	private void countEvenOdd(char character) {
		
		//Check if the character encountered is a digit or not
		if( Character.isDigit( character ) ) {
			int digit = Integer.parseInt(String.valueOf(character));
			if ( digit == 0 || digit % 2 == 0 )
				++evenCounter;
			else
				++oddCounter;
		}
	}

	/**
	 * Main function of the program that initiates execution
	 * 
	 * @param  args  	Command line arguments
	 * 
	 * @return			no return value
	 */
	public static void main(String [] args) {
		try {
				//Rebinds the specified name to a new remote object
				Naming.rebind("//localhost:"+args[0]+"/PiEvenOddRMIServer", new PiEvenOddRMIServer());
				System.out.println("PiEvenOddRMIServer bound in registry");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * Reset static variables
	 * 
	 * @return			no return value
	 */
	public void resetStaticVariablesEvenAndOdd() {
		oddCounter = 0;
		evenCounter = 0;
	}

}
