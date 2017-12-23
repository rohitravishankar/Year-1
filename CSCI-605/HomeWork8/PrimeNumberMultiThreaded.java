package HomeWork8;
/*
 *  PrimeNumberMultiThreaded.java
 * 
 *  Version: PrimeNumberMultiThreaded.java, v 1.0 2017/24/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/24/10 08:07:05
 *      Initial Revision
 *      
 */

import java.util.Stack;

/**
 * This class demonstrates the understanding of threads
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class PrimeNumberMultiThreaded extends Thread {
	public static int MAX;
	byte[] allThePrimeNumbers;
	int counter;

	PrimeNumberMultiThreaded() {
		allThePrimeNumbers = new byte[MAX];
	}

	PrimeNumberMultiThreaded(int counter , byte[] primeNumberArray) {
		this.counter = counter;
		this.allThePrimeNumbers = primeNumberArray;

	}

	/**
	 * Returns whether the number is a prime or not
	 * 
	 * @param number Number to be checked whether it is prime or not
	 * 
	 * @return       True/False whether number is prime or not
	 */
	private  boolean isPrime( int number ) {
		if( number == 0 ) {
			return false;
		}
		else if( number == 1 ) {
			return false;
		}
		else {
			for( int i = 2; i <= Math.sqrt( number ); i++  ) {
				if( number % i == 0 ) {
					return false;
				}
			}
			return true;
		}
	}

	/**
	 * Inserts into the byte array at bit level
	 * 
	 * @return       No returned value
	 */
	public void run() {
		
		//Iterating over the byte array
		for( int i = 0; i < allThePrimeNumbers.length; i++ ) {
			
			//String buffer to append true false values of bits
			StringBuffer binaryBits = new StringBuffer();
			
			//Iterating over each byte
			for( int j = 0; j < 8; j ++ ) {
				
				//Calculating each bit that represents a number
				int position = counter * 8 + j;
				if( isPrime( position ) ) {
					
					//Appending result to the string buffer
					binaryBits.append("1");
				}
				else {
					binaryBits.append("0");
				}
			}
			counter += 1;
			
			//Converting the stringbuffer value into a single byte of base 2(binary)
			allThePrimeNumbers[i] = Byte.valueOf(binaryBits.toString(), 2);
		}
	}

	public int evaluateExpression( byte[] allThePrimeNumbers ) {
		Stack<String> stackOperation = new Stack<String>();
		boolean firstCase = true;
		boolean firstPrimeEncountered = false;
		String previousOperation = "-";
		int result = 0;

		//Iterating each bit in the byte array
		for( int i = 0; i < allThePrimeNumbers.length; i++ ) {
			for( int j = 0; j < 8; j ++ ) {
				int position = i * 8 + j;
				
				// The first case is p1-p2
				if( firstCase ) {
					
					//If the first prime is found push it onto the stack
					if( isPrime( position ) && !firstPrimeEncountered ) {
						firstPrimeEncountered = true;
						stackOperation.push( Integer.toString( position ) );
					}
					
					/*
					 * If the second prime is encountered pop the first number 
					 * off the stack and flag that it isn't the first case anymore
					 */
					else if( isPrime( position ) ) {
						if( !stackOperation.isEmpty() ) {
							firstCase = false;
						}
						
						//Calculate the result and push the result onto the stack
						int secondPrime = position;
						int firstPrime = Integer.parseInt( stackOperation.pop() );
						result = ( firstPrime - secondPrime ) % MAX;
						stackOperation.push( String.valueOf( result ) );
					}
				}
				else {
					if( isPrime( position ) ) {
						
						//Pop the previous result off the stack
						int firstNumberOnStack = Integer.parseInt(stackOperation.pop());
						int secondPrime = position;

						//If the previous operation was a "-" the current operation should be "+"
						if( previousOperation.equals( "-" ) ) {
							result = ( firstNumberOnStack + secondPrime ) % MAX;
							previousOperation = "+";
							stackOperation.push( String.valueOf( result ) );
						}
						
						//Else if the previous operation was "+", the current operation should be "-"
						else {
							result = ( firstNumberOnStack - secondPrime ) % MAX;
							previousOperation = "-";
							stackOperation.push( String.valueOf( result ) );
						}
					}
				}
			}
		}
		return result;
	}

	
	/**
	 * Print each byte in the byte array
	 * 
	 * @return    No returned value
	 */
	public void printByteArray() {
		for (byte b : allThePrimeNumbers) {
			System.out.println( Integer.toBinaryString(b & 255 | 256).substring(1));
		}
	}

	/**
	 * Main function of the program
	 * 
	 * @param args   command line arguments
	 * @return       No returned value
	 */
	public static void main(String max, String thread) throws InterruptedException {
		if( thread.equals("") || max.equals("") ) {
			System.out.println("Usage: java PrimeNumberMultiThreaded <MAX> <numberOfThreads>");
		}
		else {
			MAX = Integer.parseInt(max);
			
			//Reading the threads from the user
			int numberOfThreads = Integer.parseInt( thread );
			PrimeNumberMultiThreaded[] threads = new PrimeNumberMultiThreaded[numberOfThreads];

			// If the MAX cannot be divided into equal portions for threads to work
			if( MAX % numberOfThreads != 0 ) {
				int newNumberOfThreads = numberOfThreads;
				int newMAX = MAX;

				/*
				 * We reduce the number of threads by 1 and reduce the max by a
				 * number to make it divisible by the reduced number of threads.
				 * Now, each thread handles an equal piece of work and the last thread
				 * we reduced for the calculation handles the remaining of the MAX
				 */
				newNumberOfThreads -= 1;
				int decrementValue =  newMAX % newNumberOfThreads;
				newMAX -= decrementValue;
				
				int blockHandledByThread = newMAX/newNumberOfThreads;

				int i;
				for ( i = 0; i < newNumberOfThreads ; i++ ) {	
					threads[i] = new PrimeNumberMultiThreaded( i * blockHandledByThread , new byte[blockHandledByThread] );
					threads[i].start();
				}
				threads[i] = new PrimeNumberMultiThreaded( i * blockHandledByThread, new byte[decrementValue]);
				threads[i].start();
			}
			
			// If the MAX cannot be divided into equal portions for threads to work on
			else {

				int blockHandledByThread = MAX/numberOfThreads;

				for ( int i = 0; i < numberOfThreads ; i++ ) {	
					threads[i] = new PrimeNumberMultiThreaded( i * blockHandledByThread , new byte[blockHandledByThread] );
					threads[i].start();
				}

			}
			for ( int i = 0; i < numberOfThreads ; i++ ) {
				threads[i].join();
			}
			for( int i = 0; i < numberOfThreads; i++ )  {
				threads[i].printByteArray();
			}
			
			//Create a copy of all threads into a concatenated array to evaluate the expression
			byte[] concatenatedArray = new byte[MAX];
			for ( int i = 0; i < numberOfThreads ; i++ ) {
				if( i == 0 ) {
					System.arraycopy(threads[i].allThePrimeNumbers, 0, concatenatedArray, 0, threads[i].allThePrimeNumbers.length);
				}
				else {
					System.arraycopy(threads[i].allThePrimeNumbers, 0, concatenatedArray, threads[i-1].allThePrimeNumbers.length, threads[i].allThePrimeNumbers.length);
				}
			}

			PrimeNumberMultiThreaded primeNumberMultiThreaded = new PrimeNumberMultiThreaded();

			System.out.println(primeNumberMultiThreaded.evaluateExpression(concatenatedArray));

		}
	}
}
