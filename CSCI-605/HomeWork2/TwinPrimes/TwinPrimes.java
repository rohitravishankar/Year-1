package HomeWork2;
/* 
 * TwinPrimes.java 
 * 
 * Version: TwinPrimes.java, v 1.0 2017/28/08
 * 
 * Revisions: 
 *    Revision 1.0  2017/04/09 12:19:05  
 *    Initial revision 
 */

/**
 * This program displays twin primes in a given range.
 *
 * @author      Rohit Ravishankar
 * @author		Parinitha Nagaraja
 */

public class TwinPrimes {
	
	/**
	 * Determines whether a number is prime or not
	 * 
	 * @param	number	To read the number whose primality must be checked
	 *            
	 * @return 			True if the number is a prime number, else false
	 */
	
	public boolean isPrime( int number ) {
		
		//If the number is 0 or 1 it isn't a prime number
        if( number == 0 || number == 1 ) {
            return false;
        }
        
        //To determine whether a number is a prime or not
        for( int i = 2; i <= number/2; i++ ) {
            if( number % i == 0 ) {
                return false;
            }
        }
        return true;
	}
	
	/**
	 * To find all twin primes in a given range
	 * 
	 * @param	rangeBeginning	To mark the starting number of the range
	 * @param	rangeEnd			To mark the ending number of the range
	 *            
	 * @return 					Prints all the twin prime in a given range
	 */
	
	public void findTwinPrimes( int rangeBeginning, int rangeEnd ) {
		
		//Iterating till rangeEnd-2 to ensure all numbers are within the range
		for( int i = rangeBeginning; i <= rangeEnd - 2; i++ ) {
			
			//isPrime is called on p & p+2 values so as to find twin primes 
			if( isPrime( i ) && isPrime( i+2 ) ) {
				System.out.println( "(" + i + ", " + (i+2) + ")");
			}
		}
	}
	
	/**
	 * Calling function to other functions to facilitate finding twin primes
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */

	public static void main( String[] args ) {
        int delta = 100;
        for( int index = 00; index < 1000; index += 100 )      {
                new TwinPrimes().findTwinPrimes(index, index + delta);
        }
	}
}