package HomeWork9;
/*
 *  VanishingTrolls.java
 * 
 *  Version: VanishingTrolls.java, v 1.0 2017/03/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/03/11 21:00:05
 *      Initial Revision
 *      
 */

import java.util.HashMap;

/**
 * This class demonstrates the understanding of Thread Synchronization
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class VanishingTrolls extends Thread {

	// Indicating trollNumber/trollId
	private int trollNumber;
	
	// 1 object, 1 key and multiple threads
	private static Object cookieObject = new Object();
	
	//All trolls should be able to see the same number of cookies
	private static int currNumberOfCookies;
	
	//The current number of trolls alive in the game
	private static int currNumberOfTrolls;
	
	//Hashmap to store each troll and whether it got a cookie or not
	private static HashMap<Integer, Boolean> trolls;

	public VanishingTrolls() {

	}

	public VanishingTrolls( int trollNumber ) {
		this.trollNumber = trollNumber;
	}

	/**
	 * Starts the game with the n number of trolls given by the user and 
	 * n-1 cookies
	 * 
	 * @return No value returned	
	 */
	public void run() {
		synchronized ( cookieObject ) {
			grabCookie();
		}

	}

	/**
	 * Starts the game with the n number of trolls given by the user and 
	 * n-1 cookies
	 * 
	 * @return No value returned	
	 */
	public void grabCookie() {
		
		//Iterate till the number of trolls remaining is only 1 and the trolls are still alive
		while ( currNumberOfTrolls >= 1 && trolls.get( trollNumber ) ) {
			synchronized ( cookieObject ) {	
				System.out.println( "  "+ trollNumber + "\t" + currNumberOfCookies ); 
				
				//If the number of trolls is greater than 1 and the trolls are still alive (have grabbed a cookie)
				if ( currNumberOfCookies >= 1  && trolls.get( trollNumber ) ) {
					//System.err.println(trollNumber );

					//Decrement the remaining number of cookies
					--currNumberOfCookies;

					//Invoke a wait signal on the synchronized object
					try {
						cookieObject.wait();
					}
					catch( InterruptedException e) {
						System.out.println( ": InterruptedException" );
					}										
				}
				else {
					
					//If it is not the last case display the troll who did not get a cookie this round
					if( !( currNumberOfTrolls == 1 && currNumberOfCookies == 0 ) ) {
						System.out.println();
						System.out.println( trollNumber + " did not get the cookie in this round" );
						System.out.println( "========================================" );
					}
					
					//Update the value for the troll in the hashmap
					trolls.put( trollNumber , !trolls.get( trollNumber ) );
					
					//Decrement the trolls by 1 (i.e., the troll who could not grab a cookie)
					--currNumberOfTrolls;
					
					//Reset the cookies back to 1 less than the number of trolls
					currNumberOfCookies = currNumberOfTrolls - 1;
					
					//notify the other threads/trolls
					cookieObject.notifyAll();

				}

			}			
		}
		
		//While number of remaining trolls are 0 display the winner!
		synchronized ( cookieObject ) {
			if( currNumberOfTrolls == 0 ) {
				System.out.println( "Winner is  " + trollNumber );					
			}			
		}


	}

	/**
	 * Initializes trolls and threads for the program
	 * 
	 * @param numberOfTrolls	Number of trolls/threads based on user input
	 * 
	 * @return No value returned	
	 */
	public void init( int numberOfTrolls ) {
		System.out.println( "=========================" );
		System.out.println( "Trolls " + "\t" + "Cookies Available");
		System.out.println( "=========================" );
		
		//Create a hash map entry for each troll and start inform all the threads to start
		for( int i=1; i <= numberOfTrolls; i++ ) {
			trolls.put( i, true );		
			new VanishingTrolls( i ).start();
		}
	}


	/**
	 * Main function of the program
	 * 
	 * @param args	Command line arguments (ignored)
	 * 
	 * @return No value returned	
	 */
	
	public static void main( String[] args ) {
		
		//Creating an object of the Vanishing Trolls class
		VanishingTrolls vanishingTrolls = new VanishingTrolls();
		
		//Reading number of trolls/threads as a command line argument 
		int numberOfTrolls = Integer.parseInt(args[0]);
		
		//Initializing current number of trolls in order to use it for future processing
		currNumberOfTrolls = numberOfTrolls;
		
		/*
		 * Initializing current number of cookies to be 1 lesser than number
		 * of trolls for future processing
		 */
		currNumberOfCookies = numberOfTrolls - 1;
		
		//Creating a hash map of the trolls and status whether the troll has grabbed a cookie or not
		trolls = new HashMap<>( numberOfTrolls );
		
		//Initializing the game
		vanishingTrolls.init(numberOfTrolls);		
	}

}
