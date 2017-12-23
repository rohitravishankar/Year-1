
/* 
 * P.java 
 * 
 * Version: P.java, v 1.0 2017/29/08
 * 
 * Revisions: 
 *    Revision 1.0  2017/29/08 16:34:03  
 *    Initial revision 
 */

import java.math.BigInteger;

/**
 * This program prints the following series using an iterative solution
 * P(0) := 0; for n = 0; 
 * P(1) := 1; for n = 1; 
 * P(n) := 2 * P(n-1) + P(n-2); for n ≥ 2
 *
 * @author Rohit Ravishankar
 */
public class P {

	/**
	 * Facilitates printing the series
	 * 
	 * @param	numberOfTerms	To read the number of terms to be printed
	 *            
	 * @return 					Prints the solution to return success
	 */

	public static int printSolution( int numberOfTerms ) {
		System.out.println( "p(0) = 0\np(1) = 1" );
		
		//a holds the P(n-2) value
		BigInteger a = new BigInteger( "0" );
		
		//b holds the P(n-1) value
		BigInteger b = new BigInteger( "1" );
		
		//c calculates the required P(n) value in the series
		BigInteger c;	
		for ( int i = 2; i <= numberOfTerms; ++i ) {
			
			//signifies the calculation of 2 * P(n-1) + P(n-2)
			c = ( b.multiply( new BigInteger( "2" ) ) ).add( a );
			a = b;	//reassigns variable for the next computation
			b = c;	//reassigns variable for the next computation
			System.out.println( "p(" + i + ") = " + c );
		}
		return 0;
	}

	/**
	 * Calling function to other functions to facilitate printing the series
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */

	public static void main( String[] args ) {
		printSolution( 100 );
	}
}

