package HomeWork10;
/*
 *  Consumer.java
 * 
 *  Version: Consumer.java, v 1.0 2017/09/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/09/11 08:11:09
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the understanding of Thread Synchronization
 * 
 * @author Rohit Ravishankar
 * @author Parinitha Nagaraja
 *
 */

public class Consumer extends Thread {

	private final int STOP_CONSUMPTION = 10;
	private CircularRingBuffer circularRingBuffer;
	private int threadNumber;

	private static Object o = new Object();
	private static int totalNumberOfConsumedItems = 0;

	public Consumer() {

	}

	public Consumer( CircularRingBuffer circularRingBuffer, int threadNumber ) {
		this.circularRingBuffer = circularRingBuffer;
		this.threadNumber = threadNumber;
	}

	/**
	 * Consumes values from the ring buffer
	 * 
	 * @return No value returned
	 */
	public void run() {
		int value = 0;
		while(true) {
			System.out.println("Consumer - Consumer #" + threadNumber + " tried to enter the synchronized block");

			//To ensure that only those threads that can consume the remaining spaces compete
			if( ( circularRingBuffer.size - circularRingBuffer.numberOfElements() - threadNumber ) >= 0 &&
					circularRingBuffer.numberOfElements() != 0 ) {

				//All the threads that can consume the buffer elements wait at the synchronized block
				synchronized (o) {
					System.out.println("Consumer - Consumer #" + threadNumber + " managed enter the synchronized block");

					int iterator = threadNumber;

					//jth consumer consumes j items 
					while( iterator > 0 ) {
						value = circularRingBuffer.delete();

						//To tackle the case when consumer greedily tries to remove element not there
						if( value != -1 ) 
							System.out.println( "\nConsumer #" + threadNumber + " consumed : " + value );
						++totalNumberOfConsumedItems;
						--iterator;
					}
					if ( totalNumberOfConsumedItems >= STOP_CONSUMPTION ) {
						break;
					}

				}
			}
		}
	}
}
