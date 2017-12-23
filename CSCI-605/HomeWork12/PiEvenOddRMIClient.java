package HomeWork12;
/*
 *  PiEvenOddRMIClient.java
 * 
 *  Version: PiEvenOddRMIClient.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/27/11 10:29:05
 *      Initial Revision
 *      
 */

import java.io.*;
import java.rmi.Naming;
import java.util.Scanner;

/**
 * This program calculates the number of Even-Odd values of Pi using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class PiEvenOddRMIClient {
	
	
	/**
	 * Main code that defines client side logic
	 * 
	 * @param args	Command line arguments
	 * 
	 * @return		no return value
	 */
	
	public static void main(String [] args) {
		
		try {
			 PiEvenOddRMIInterface lookUp;
			
			//Get the name of the file from the user 
			Scanner scanner = new Scanner(System.in);
			System.out.print("Enter the path of the file: ");
			String fileName = scanner.next();
			scanner.close();
			
			//Connecting to the server
			System.out.println( "Connecting to the server..........." );
			
			//Copy contents to a character array
			char[] contentsOfFile = getCharacterArray( fileName );
			System.out.println();
			
			//Looking Up the interface for the necessary method
			lookUp = (PiEvenOddRMIInterface) Naming.lookup("//localhost:"+args[0]+"/PiEvenOddRMIServer");
			
			//Sending information to the server
			lookUp.calculateEvenOddPiValues( contentsOfFile );
			
			//Waiting for server response
			System.out.println();
			System.out.println( "Waiting for the server to respond..........." );
			
			
			//Getting the values from the server
			long oddCounter = lookUp.getOddCount();
			long evenCounter = lookUp.getEvenCount();
			double oddEvenRatio = ( double ) oddCounter/evenCounter;
			
			//reset the variables at server end prior to the next execution
			lookUp.resetStaticVariablesEvenAndOdd();
			
			//Printing out the values received from the server
			System.out.println( "even = " + evenCounter + "\nodd = " + oddCounter + "\nodd/even = " + oddEvenRatio + "\n" );
			
			
			
	         
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * Returns character array of the file contents
	 * 
	 * @param fileName	file name for which we are creating the character array 
	 * 
	 * @return			no return value
	 */
	
	private static char[] getCharacterArray( String fileName ) throws IOException {
		
		//Open the file and read all the contents to a character array
		File file = new File( fileName );
		BufferedReader bufferedReader = new BufferedReader( new FileReader( file ) );
		char[] buffer = new char[(int) file.length()];
		while( bufferedReader.read(buffer) != -1 ) {
		}
		bufferedReader.close();
		return buffer;
	}

}
