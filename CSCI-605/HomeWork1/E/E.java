package HomeWork1;
/* 
 * E.java 
 * 
 * Version: E.java, v 1.0 2017/01/09
 * 
 * Revisions: 
 *    Revision 1.0  2017/01/09 21:29:05  
 *    Initial revision 
 */

/**
 * This program calculates |fn(0.5) - f∞(0.5)| < delta, for delta>0.
 *
 * @author		Rohit Ravishankar
 */

public class E {

	/**
	 * Calculates powers for a number
	 * 
	 * @param	number	Number whose power must be calculated
	 * @param	power	Holds the value of the power
	 *            
	 * @return 			number raised to a certain power
	 */
	
	public static double calculatePowerOfN ( double number, double power ) {
		double term = 1;
		if( power == 0 ) {
			return 1;
		} else {
			
			//To calculate a number to a certain power
			for( int i = 1; i <= power; i++ ) {
				term *= number;	//multiplies previous term with the number
			}
		}
		return term;
	}
	
	/**
	 * Calculates function value at infinity for a number
	 * 
	 * @param	firstTerm	First term of the GP series
	 * @param	commonRatio	Common Ratio for the GP series
	 *            
	 * @return 				function value for the GP at infinity
	 */
	
	public static double functionValueAtInfinity( double firstTerm, 
			double commonRatio ) {
		return firstTerm / ( 1 - commonRatio ); //S∞ = a/1-r
	}
	
	/**
	 * Calculates absolute value for a number
	 * 
	 * @param	number	Number whose absolute must be calculated
	 *            
	 * @return 			number raised to a certain power
	 */
	
	public static double calculateAbsoluteValue( double number ) {
		return number < 0 ? ( -number ) : number;
	}
	
	/**
	 * Calculates absolute value for a number
	 * 
	 * @param	x	The number the function must be calculated at
	 *            
	 * @return 		no value returned
	 */
	
	private static void f( double x ) {
		int n = 0;
		double functionOfN = 0, differenceBetweenFnAndFinfinity = 1;
		double delta = 0.00003;
		
		//Loop until |fn(x) - f∞(x)| < delta
		while( differenceBetweenFnAndFinfinity >= delta ) {
			functionOfN += calculatePowerOfN( ( -x ), n );
			differenceBetweenFnAndFinfinity = calculateAbsoluteValue(
					functionOfN - functionValueAtInfinity( 1.0, ( -x ) ) );
			n++;
		}
		double lastAddedTerm  = calculatePowerOfN( (-0.5), n-1);
		System.out.println("f(0.5) = " + functionOfN + "	" + n + "	" + 
				lastAddedTerm);
	}
	
	/**
	 * Calling function to other functions to find necessary values
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */
	
	public static void main( String[] args ) {
		f(0.5);
	}

}
