package HomeWork3;
/*
 *  X.java
 * 
 *  Version: X.java, v 1.0 2017/13/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/13/09 15:10:03
 *      Initial Revision
 *      
 */

/**
 * This program is to understand control structures
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */
class X {

	public static void main( String args[] ) {

		int n = 0;

		here:
            
			while ( true )  {
                
				/*
				 * Iteration 1. n is equal to 0, which satisfies the
				 *              conditions and enters the while loop
				 * 
				 * Iteration 2. n is equal to 2, which satisfies the
				 *              conditions and enters the while loop
				 *              
				 * Iteration 3. n is equal to 5, which does not satisfy the
				 *              conditions and hence does not enter
				 *              the while loop
				 */
				while ( ( ( n != 3 ) || ( n != 5 ) ) && ( n < 4 ) )  {
					
					/*
					 * Iteration 1. n is pre incremented( which makes n = 1 )
					 *              and compared against 0 which returns false
					 *            
					 * Iteration 2. n is pre incremented( which makes n = 3 )
					 *              and compared against 0 which returns false
					 * 
					 */
					if ( ++n == 0 )
						System.out.println("a/	n is " + n );
					
					/*
					 * Iteration 1. n = 1 is compared with 1 which returns true
					 *              n is post incremented 
					 *              n is now 2
					 *              b/ n is 2 is printed
					 *              While loop continues with n = 2
					 * 
					 * Iteration 2. n = 3 is compared with 1 which returns false
					 *              n is post incremented 
					 *              n is now 4
					 */
					else if ( n++ == 1 )    {
						System.out.println("b/	n is " + n );
					} 
					
					/*
					 * Iteration 1. Does not execute
					 * 
					 * Iteration 2. n = 4 is compared with 2 which returns false
					 *              n is post incremented 
					 *              n is now 5
					 */
					else if ( n++ == 2 )
						System.out.println("c/	n is " + n );
					
					/*
					 * Iteration 1. Does not execute
					 * 
					 * Iteration 2. Since, none of the if-else if are executed,
					 *              else block gets executed and the following
					 *              is printed  d/  n is 5
					 */
					else 
						System.out.println("d/	n is " + n );
					
					/*
					 * Iteration 1. Prints 	executing break here
					 * 
					 * Iteration 2. Prints 	executing break here
					 */
					System.out.println("	executing break here");

				}
                
				/*
				 *  Iteration 3. n is 5
				 *               n%2 is not equal to 0
				 *               The expression after : gets evaluated
				 *               n%3 is 2 which is not equal to 0
				 *               and evaluates to true. 
				 *               Prints 3.
				 */
				
				System.out.println( n % 2 == 0 ?
						( n == 4 ? "=" : "!" )
						: ( n % 3 != 0 ? "3" : "!3" ));
				/*
				 * The break statement terminates the statement
				 * it does not transfer the flow of control to the label
				 */
				
				break here;
			}
	}
}