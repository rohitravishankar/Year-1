package HomeWork10;
/*
 *  ReadersAndWriter.java
 * 
 *  Version: ReadersAndWriter.java, v 1.0 2017/08/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/03/11 21:00:05
 *      Initial Revision
 *      
 */

import java.io.*;
import java.util.concurrent.Phaser;
import java.util.concurrent.Semaphore;

/**
 * This class demonstrates the understanding of Thread Synchronization
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class ReadersAndWriter extends Thread {

	//Buffer to where the writer writes
	static byte[] buffer;
	
	//Array of reader threads
	static ReadersAndWriter threads[];
	static Phaser phaser;
	static boolean isFirstWrite = true;
	static int numberOfBytesRead;
	static FileInputStream fileInputStream;
	static int numberOfReaders;
	static int phase;
	
	private static Semaphore semaphore;
	
	//Buffer size that determines the number of bytes read by writer from the file
	private static final int bufferSize = 1024;

	//Thread attributes
	int threadNumber;
	FileOutputStream fos;
	boolean isWriter;
	boolean isReadyToWrite;

	public ReadersAndWriter() {
	}

	public ReadersAndWriter( int threadNumber, boolean isWriter ) {
		this.threadNumber = threadNumber;
		this.isWriter = isWriter;
	}

	public ReadersAndWriter(int threadNumber, boolean isWriter, FileOutputStream fos, boolean isReadyToWrite) {
		this.threadNumber = threadNumber;
		this.isWriter = isWriter;
		this.fos = fos;
		this.isReadyToWrite = isReadyToWrite;
	}

	/**
	 * To start the process of writing, i.e., writing from file to the buffer
	 * 
	 * @param filePath   Input file path
	 * @param numReaders Number of reader threads
	 * 
	 * @return     		No return value
	 */
	public void startProcess( String filePath, int numReaders ) throws IOException {
		numberOfReaders = numReaders;
		File file = new File(filePath);
		fileInputStream = new FileInputStream(file);		
		buffer = new byte[bufferSize];
		
		//Creates the writer thread
		ReadersAndWriter writerThread = new ReadersAndWriter(0, true);
		
		//Registering the writer thread with the phaser
		phaser = new Phaser();
		phaser.register();
		
		//Start the process of writing
		writerThread.start();

	}

	/**
	 * To start the process of reading, i.e., reading from buffer to files
	 * 
	 * @return     		No return value
	 */
	public void startReading() throws FileNotFoundException {

		//Starts the process of reading
		threads = new ReadersAndWriter[numberOfReaders];
		
		//Semaphore to allow only n/2 readers at once
		semaphore = new Semaphore( numberOfReaders/2 );
		FileOutputStream fileOutpustream;
		
		//Creating readers
		for (int i = 0; i < numberOfReaders; i++) {
			
			//Creating a file to be written to by each reader
			File file = new File("ReaderThreadFile" + i + ".txt");
			fileOutpustream = new FileOutputStream(file, true);
			threads[i] = new ReadersAndWriter(i, false, fileOutpustream, true);
			
			//Registering the readers with the phaser
			phaser.register();
			threads[i].start();
		}
	}

	/**
	 * To read from the file, copy to buffer and write to the files
	 * 
	 * @return     		No return value
	 */
	public void run() {
		
		//if its a writer thread
		if (isWriter) {
			try {
				
				//If the write is the first write
				if ( isFirstWrite ) {
					
					//Read from the file and write to the buffer
					numberOfBytesRead = fileInputStream.read(buffer);
					System.out.println("Writing " + phase + " completed");
					isFirstWrite = false;
					phase = phaser.getPhase();
					
					//Start the process of reading from the buffer and writing to files
					startReading();
					
					//Wait for all the reader threads and then advance
					phaser.arriveAndAwaitAdvance();
					System.out.println("Reading " + phase + " completed");
				}
				while ( (numberOfBytesRead = fileInputStream.read(buffer) ) != -1) {					
					phase = phaser.getPhase();
					System.out.println("Writing " + phase + " completed");
					
					//Mark all the threads as ready to write
					for ( int i=0; i< numberOfReaders; i++ ) {
						threads[i].isReadyToWrite = true;						
					}
					
					//Wait for all the threads to complete writing to file and advance
					phaser.arriveAndAwaitAdvance();
					System.out.println("Reading " + phase + " completed");
					
				}

			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		//if readers
		if( !isWriter ) {
			while(true) {
				
				//Write once flag is set
				if( isReadyToWrite == true ) {
					try {
						
						//Writing the file to buffer
						writeToFileFromBuffer();
						
						//Flag once the writing is complete
						isReadyToWrite = false; 
						
						//Wait for all the threads before advancing
						phaser.arriveAndAwaitAdvance();
					} catch (FileNotFoundException | InterruptedException e) {
						e.printStackTrace();
					}
				}
				
				//If the bytes read returned -1, i.e., EOF
				if ( numberOfBytesRead == -1 ) {
					System.out.println("Reader " + threadNumber + " Number of bytes read " + numberOfBytesRead);
					
					//Deregister all the reader threads
					phaser.arriveAndDeregister();
					break;
				}
				
			}
			
		}
	}
	
	/**
	 * To process writing, i.e., writing from buffer to files
	 * 
	 * @return     		No return value
	 */
	public void writeToFileFromBuffer() throws FileNotFoundException, InterruptedException {
		
		//Only n/2 readers should read simultaneously
		semaphore.acquire();
		try {
			fos.write( buffer );
		} catch (Exception e) {
			e.printStackTrace();
		}
		semaphore.release();
	}


}
