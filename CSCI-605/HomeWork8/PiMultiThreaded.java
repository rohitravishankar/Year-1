package HomeWork8;
/*
 *  PiMultiThreaded.java
 * 
 *  Version: PiMultiThreaded.java, v 1.0 2017/24/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/24/10 08:07:05
 *      Initial Revision
 *      
 */
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * This class demonstrates the understanding of threads
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class PiMultiThreaded extends Thread{
	static long totalEven = 0;
	static long totalOdd = 0;
	
	long evenCounter = 0;
	long oddCounter = 0;
	byte[] buffer;
	
	public PiMultiThreaded() {		
	}
	
	public PiMultiThreaded( byte[] buffer ) {
		this.buffer = buffer;
	}		
	
	/**
	 * Count even odd occurrences if command line arguments are specified
	 * 
	 * @param filePath	    File path to read pi value
	 * @param numOfThreads	Number of threads
	 * 
	 * @return No value returned
	 */
	public void CountOddEvenInPiForCommandLineArgs( String filePath, 
			String numOfThreads ) throws IOException {
		File file = new File( filePath );
		FileInputStream fileInputStream = null;
		BufferedInputStream bis = null;
		int size = (int) file.length();
		int numberOfThreads = Integer.parseInt(numOfThreads);
		
		//Calculate the buffer size
		int bufferSize = size/numberOfThreads;
		
		//Create a buffer for each thread
		byte[] buffer = new byte[bufferSize];

		try {
			fileInputStream = new FileInputStream( filePath );
			bis = new BufferedInputStream( fileInputStream );
			
			PiMultiThreaded threads[] = new PiMultiThreaded[numberOfThreads];
			int counter = 0;
			
			while ( bis.read(buffer) != -1 && counter < numberOfThreads) {
				
				//Create a thread
				threads[counter] = new PiMultiThreaded( buffer );	
				
				//Start the thread to calculate number of odd and even numbers
				threads[counter].start();
				
				++counter;
				buffer = new byte[bufferSize];
			}
			
			//Wait for all threads to finish
			for( int i = 0; i < threads.length; i++ ) {
				try{
					threads[i].join();
				}
				catch(InterruptedException e){
					System.out.println("Interrupted!");
				}
			}
			
			//Add even and odd counters from all the threads
			for( int i = 0; i < threads.length; i++ ) {				
				totalEven += threads[i].evenCounter;
				totalOdd += threads[i].oddCounter;
			}
			
			//Print the result
			System.out.println( "even: " + totalEven );
			System.out.println( "odd: " + totalOdd );
			double result = (double) totalOdd/totalEven;
			System.out.println( "odd/even: " + result );
			
		}

		catch ( FileNotFoundException e ) {
			System.out.println(e.getMessage() );
		}

		catch ( IOException e ) {
			System.out.println(e.getMessage() );
		}

		finally {
			if( fileInputStream != null )
				fileInputStream.close();
			if( bis != null )
				bis.close();
		}

	}
	
	/**
	 * Count even odd occurrences for each thread and increments 
	 * even odd counter
	 * 
	 * 
	 * @return No value returned
	 */
	public void run() {		
		String characters = new String( buffer );
	    for( int i = 0; i < characters.length(); i++ ) {
	    	char character = characters.charAt(i);
	    	//Check if the character encountered is a digit or not
			if( Character.isDigit( character ) ) {
				int digit = Integer.parseInt(String.valueOf( character ));
				if ( digit == 0 || digit % 2 == 0 )
					++evenCounter;
				else
					++oddCounter;
			}
	    }		
	}
	
	
}
