package HomeWork10;
/*
 *  Producer.java
 * 
 *  Version: Producer.java, v 1.0 2017/09/11
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

public class Producer extends Thread {
	private CircularRingBuffer circularRingBuffer;
	private int threadNumber;

	private final int STOP_PRODUCTION = 10;

	private static int totalNumberOfProducedItems = 0;
	private static Object o = new Object();

	public Producer() {

	}

	public Producer( CircularRingBuffer circularRingBuffer, int threadNumber ) {
		this.circularRingBuffer = circularRingBuffer;
		this.threadNumber = threadNumber;
	}

	/**
	 * Produces values and puts them into the ring buffer
	 * 
	 * @return No value returned
	 */
	public void run() {
		while( true ) {
			System.out.println("Producer - Producer #" + threadNumber + " tried to enter the synchronized block");

			//To ensure that only those threads that can fill the remaining spaces compete
			if( ( circularRingBuffer.size - circularRingBuffer.numberOfElements() - threadNumber ) >= 0 ) {

				//All the threads that can fill the remaining spaces in the buffer wait at the synchronized block
				synchronized ( o ) {
					System.out.println("Producer - Producer #" + threadNumber + " managed to enter the synchronized block");

					int iterator = threadNumber;

					//ith producer produces i items
					while( iterator > 0 ) {
						int number = produce();
						System.out.println( "\nProducer #" + threadNumber + " produced : " + number );
						circularRingBuffer.insert( number );

						// To increment the total produced items in order to break the production
						++totalNumberOfProducedItems;
						--iterator;
					}
					if( totalNumberOfProducedItems >= STOP_PRODUCTION  ) {
						break;
					}
				}
			}

		}
	}

	/**
	 * Produces a random value between 0 and 100
	 * 
	 * @return Random value between 0 and 100
	 */
	public int produce() {
		int number = ( int ) (Math.random() * 100);
		return number;
	}
}
