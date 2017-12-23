package HomeWork10;
/*
 *  CircularRingBuffer.java
 * 
 *  Version: CircularRingBuffer.java, v 1.0 2017/09/11
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

public class CircularRingBuffer {

	public static int size;
	public static int front;
	public static int rear;
	public static int bufferLength;
	public static int[] buffer;

	public CircularRingBuffer( int size ) {
		this.size = size;
		front = 0;
		rear = size;
		bufferLength = 0;
		buffer = new int[size];
	}

	/**
	 * Returns whether the buffer is empty or not
	 * 
	 * @return true/false whether the buffer is empty or not
	 */
	public boolean isEmpty() {
		return bufferLength == 0;
	}

	/**
	 * Returns whether the buffer is full or not
	 * 
	 * @return true/false whether the buffer is full or not
	 */
	public boolean isFull() {
		return bufferLength == size;
	}

	/**
	 * To insert an item into a buffer
	 * 
	 * @param value Value to insert into the buffer
	 * 
	 * @return      Value that has been added/ -1 if the item cannot be inserted
	 */
	public synchronized int insert( int value ) {
		if( !isFull() ) {
			++bufferLength;
			rear = ( rear + 1 ) % size;
			buffer[rear] = value;
			return value;
		}
		return -1;
	}

	/**
	 * To remove an item into a buffer
	 * 
	 * @return      Value that has been removed/ -1 if the item cannot be removed
	 */
	public synchronized int delete() {
		if( !isEmpty() ) {
			--bufferLength;
			front = ( front + 1 ) % size;
			return buffer[front];
		}
		return -1;
	}

	/**
	 * Returns number of elements in the buffer
	 * 
	 * @return   Number of items in a buffer
	 */
	public int numberOfElements() {
		return bufferLength;
	}

	/**
	 * Prints the items in the buffer 
	 * 
	 * @return No return value
	 */
	public void display() 
	{
		System.out.print( "\nBuffer : ");
		for (int i = 0; i < size; i++)
			System.out.print( buffer[i] +" ");
		System.out.println();    
	}

}
