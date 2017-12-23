package HomeWork7;
/*
 *  PiEvenOdd.java
 * 
 *  Version: PiEvenOdd.java, v 1.0 2017/17/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/10 23:07:05
 *      Initial Revision
 *      
 */

import java.io.*;
import java.util.Scanner;

/**
 * This class demonstrates the understanding of I/O
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class PiEvenOdd {
	static long startTime = System.currentTimeMillis();

	static long evenCounter = 0;
	static long oddCounter = 0;
	
	/**
	 * Main function of the program
	 * 
	 * @param args	Command line arguments (ignored)
	 * 
	 * @return No value returned	
	 * 
	 * @exception	IOException if the File does not exist
	 */
	
	public static void main(String[] args) throws IOException {
		
		//If the arguments to the program are supplied as command line arguments
		if ( args.length >= 1 ) {
			CountOddEvenInPiForCommandLineArgs(args[0]);
		}
		
		//If the arguments to the program are supplied through standard input
		else {
			CountOddEvenInPiForStdin();
		}
		
		//Print the outputs
		printOutput();
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Time Taken: " + totalTime + "ms");

	}
	
	/**
	 * Count the number of even odd occurances in a file if the input is using standard input
	 * 
	 * @return No return value
	 */

	private static void CountOddEvenInPiForStdin() {
		Scanner scanner = new Scanner( System.in );
		int i = 0;
		String  str = scanner.next();
		
		//Put all the characters in the file in a character array
		char[] characterArray = str.toCharArray();
		while ( i < characterArray.length ) {
			//For each character check if it is odd or even
			countEvenOdd( characterArray[i] );
			i++; 
		}
		scanner.close();

	}

	/**
	 * Counts number of times even odd numbers occur
	 * 
	 * @param character	Character to be checked if it is even or odd	
	 * 
	 * @return No value returned
	 */
	private static void countEvenOdd(char character) {
		
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
	 * Prints the even and odd occurances
	 * 
	 * @return No returned value
	 */
	private static void printOutput() {
		System.out.println( "even = " + evenCounter );
		System.out.println( "odd = " + oddCounter );
		double result = (double) oddCounter/evenCounter;
		System.out.println( "odd/even = " + result );
	}
	
	/**
	 * Count eve odd occurances if command line arguments are specified
	 * 
	 * @param filePath	File path to read pi value
	 * 
	 * @return No value returned
	 */
	private static void CountOddEvenInPiForCommandLineArgs(String filePath) throws IOException {
		Reader fileReader = null;

		try {
			fileReader = new FileReader(filePath);
			
			//Reading the file from command line args
			int data = fileReader.read();
			char character;
			while ( data  != -1 ) {
				countEvenOdd( (char) data );
				data = fileReader.read();
			}
			
		}

		catch ( FileNotFoundException e ) {
			System.out.println(e.getMessage() );
		}

		catch ( IOException e ) {
			System.out.println(e.getMessage() );
		}

		catch ( NumberFormatException e) {
			System.out.println(e.getMessage() );
		}

		finally {
			if( fileReader != null )
				fileReader.close();
		}

	}

}
