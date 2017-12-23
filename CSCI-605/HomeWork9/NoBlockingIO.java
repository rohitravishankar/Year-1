package HomeWork9;
/*
 *  NoBlockingIO.java
 * 
 *  Version: NoBlockingIO.java, v 1.0 2017/04/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/04/11 08:07:05
 *      Initial Revision
 *      
 */
import java.io.*;

/**
 * This class demonstrates the understanding of Thread Synchronization
 * 
 * @author Rohit Ravishankar
 * @author Parinitha Nagaraja
 *
 */


public class NoBlockingIO extends Thread{
	
	//Divide the reads based on number of threads
	public static final int NUMBER_OF_THREADS = 4;

	//Total even/odd count
	static long totalEven = 0;
	static long totalOdd = 0;
	
	//Static object on which the block is synchronized
	static Object object = new Object();
	
	//Buffer 1 on which all the calculation happens
    static byte[] finalBuffer;
    
    //To ensure the output is sequential
	static int readCount = 0;
	
	//Creating an array of threads
	NoBlockingIO threads[] = new NoBlockingIO[NUMBER_OF_THREADS];
	
	//To mark a thread id
	int id;
	
	//Thread buffered reader
	BufferedReader brr = null;
	
	//Individual buffer for each thread
	byte[] buffer;
	
	//To have the path of the data file
	static String filePath = "";
	
	//BufferedReader object from the input
	BufferedReader in;
	
	//Each buffer size
	static int bufferSize;

	public NoBlockingIO() {		
		
	}

	public NoBlockingIO( int id, byte[] buffer , BufferedReader in  ) {
		this.id = id;
		this.buffer = buffer;
		this.brr = in;
	}

	public NoBlockingIO( BufferedReader br ) {
		this.in = br;
	}

	/**
	 * Initiate the process of reading
	 * 
	 * @param filePath	    File path to read
	 * @param finalBuffer	Buffer from the input 
	 * 
	 * @return No value returned
	 */
	public void read( String filePath ) throws IOException {
		
		//File object with argument as a filePath
		File file = new File( filePath );

		//Calculating length to decide which part should each thread take
		int size = (int) file.length();
		
		this.filePath = filePath;

		//Calculate the buffer size
		bufferSize = size/NUMBER_OF_THREADS;

		//Create a buffer for a thread
		byte[] inbuffer = new byte[bufferSize];

		//Allowing the final buffer to be available globally
		finalBuffer = new byte[bufferSize];

		//The first thread read should be blocking
		threads[0] = new NoBlockingIO( 0,  inbuffer , in );
		threads[0].start();

	}

	/**
	 * Simulation of no blocking IO
	 * 
	 * @return No value returned
	 */
	public void run() {	
		
		//The thread is reading
		try {
			read1( id );
		} catch (IOException e1) {
			e1.printStackTrace();
		}

		//If the first thread, spawn multiple threads 
		if (id == 0) {
			for ( int i = 1; i < NUMBER_OF_THREADS; i++) {
				byte[] inbuffer = new byte[bufferSize];
				threads[i] = new NoBlockingIO( i, inbuffer , brr );
				threads[i].start();
			}
		}

		//Synchronized on object for processing the data sequentially
		synchronized ( object ) {
			
			//Describes the thread which has finished reading
			System.out.println( id + " has finished reading. ");
			
			//To ensure that the thread data is processed sequentially
			while ( readCount != id ) {
				System.out.println( id + " is waiting to process the data. ");
				try {
					object.wait();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}	
			
			//To ensure that the thread data is processed sequentially
			if( readCount == id ) {
				System.out.println( id + " is being processed.");
				System.arraycopy( this.buffer , 0, finalBuffer, 0, this.buffer.length );
				++readCount;
				countEvenOdd( finalBuffer );				
				object.notifyAll();				
			}
			
			//If all the threads have been processed print the result
			if( readCount  == NUMBER_OF_THREADS ) {
				
				//Print the result
				System.out.println( "even: " + totalEven );
				System.out.println( "odd: " + totalOdd );
				double result = (double) totalOdd/totalEven;
				System.out.println( "odd/even: " + result );
			}
		}

	}

	/**
	 * Read different parts of the file from threads
	 * 
	 * @param id Thread number
	 * 
	 * @return No return value
	 * 
	 * @throws IOException If file is not found
	 */
	public void read1( int id ) throws IOException {
		RandomAccessFile randomFile = new RandomAccessFile( filePath, "r");	
		long offset = bufferSize * id;			
		randomFile.seek( offset );
		try {
			randomFile.read( buffer );
		} catch (IOException e) {
			e.printStackTrace();
		}

	}
	
	/**
	 * To count even/odd occurances within input file
	 * 
	 * @param inputBuffer The input buffer to calculate even/odd digits
	 * 
	 * @return	No returned value
	 */
	private  void countEvenOdd( byte[] inputBuffer ) {
		
		//Convert input buffer into a string of characters
		String characters = new String( inputBuffer );
		
		//Iterating over the entire length of the string
		for( int i = 0; i < characters.length(); i++ ) {
			char character = characters.charAt(i);
			
			//Check if the character encountered is a digit or not
			if( Character.isDigit( character ) ) {
				int digit = Integer.parseInt(String.valueOf( character ));
				if ( digit == 0 || digit % 2 == 0 )
					++totalEven;
				else
					++totalOdd;
			}

		}
		System.out.println("EVEN COUNT: " + " thread id: " + id + " count: " + totalEven );
		System.out.println("ODD COUNT: " + " thread id: " + id + " " + totalOdd );
	}
}
