package HomeWork10;
/*
 *  CircularBufferTest.java
 * 
 *  Version: CircularBufferTest.java, v 1.0 2017/09/11
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

public class CircularBufferTest {

	/**
	 * Tests the producer consumer problem
	 * 
	 * @return No value returned
	 */
	public static void main(String args[]) {
		int sizeOfBuffer = Integer.parseInt(args[0]);
		int numberOfProducerThreads = Integer.parseInt(args[1]);
		int numberOfConsumerThreads = Integer.parseInt(args[2]);


		CircularRingBuffer circularRingBuffer = new CircularRingBuffer( sizeOfBuffer );

		Producer[] producers = new Producer[numberOfProducerThreads+1];
		Consumer[] consumers = new Consumer[numberOfConsumerThreads+1];

		//Creates producers
		for( int i = 1; i <= numberOfProducerThreads; i++ ) {
			producers[i] = new Producer( circularRingBuffer , i );
			producers[i].start();
		}

		//Creates consumers
		for( int i = 1; i <= numberOfConsumerThreads; i++ ) {
			consumers[i] = new Consumer( circularRingBuffer , i );
			consumers[i].start();
		}
	}
}
