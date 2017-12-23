package HomeWork12;
/*
 *  BackToTheFutureServer.java
 * 
 *  Version: BackToTheFutureServer.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.Naming;

/**
 * This program implements the Hangman Game using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class BackToTheFutureServer {
	
	/**
	 *  Implements the back to the future game using the implementation function
	 *  
	 *  @param 	args				Command line arguments
	 *  
	 *  @return					No return value
	 */
	public static void main( String args[] ) {
		try {
			BackToTheFutureInterface obj = new BackToTheFutureImpl();
			Naming.rebind("//localhost:"+args[0]+"/BackToTheFuture", obj);
			System.out.println("BackToTheFuture bound in registry");
			
		}
		catch( Exception ex) {
			System.out.println("BackToTheFutureImpl error : "+ex.getMessage());
			ex.printStackTrace();
		}
	}

}
