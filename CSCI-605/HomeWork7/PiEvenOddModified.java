package HomeWork7;
/*
 *  PiEvenOddModified.java
 * 
 *  Version: PiEvenOddModified.java, v 1.0 2017/17/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/10 23:07:05
 *      Initial Revision
 *      
 */
import java.io.*;

/**
 * This class demonstrates the understanding of I/O
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class PiEvenOddModified {
	
	static long startTime = System.currentTimeMillis();

	static long evenCounter = 0;
	static long oddCounter = 0;
	
	
    private static final int BUFFSIZE = 8 * 1024;
    
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
	
	private static void CountOddEvenInPiForStdin() throws IOException {
		BufferedReader bufferedReader = null;
		try {
			
			//Reading the input in chunks of BUFFSIZE
			bufferedReader = new BufferedReader(new InputStreamReader(System.in), BUFFSIZE);
			int i = 0;
			String  str = bufferedReader.readLine();
			
			//Put all the characters in the file in a character array
			char[] characterArray = str.toCharArray();
			while ( i < characterArray.length ) {
				
				//For each character check if it is odd or even
				countEvenOdd( characterArray[i] );
				i++; 
			}
		}

		catch ( IOException e ) {
			System.out.println(e.getMessage() );
		}
		
		catch ( NumberFormatException e) {
			System.out.println(e.getMessage() );
		}
		
		finally {
			if( bufferedReader != null )
				bufferedReader.close();
		}

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
			fileReader = new BufferedReader(new FileReader(filePath), BUFFSIZE);
			
			//Reading the file from command line args of a BUFFSIZE chunk
			int data = fileReader.read();
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
