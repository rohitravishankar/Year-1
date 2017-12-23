/*
 *  MySortedList.java
 * 
 *  Version: MySortedList.java, v 1.0 2017/04/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/04/10 10:10:05
 *      Initial Revision
 *      
 */

import java.util.Comparator;
import java.util.Vector;

/**
 * This class demonstrates the use of inheritance
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class MySortedList<T extends Comparable<T>> implements MyStorage<T> {
	
	Vector<T> vector;
	
	public MySortedList() {
		vector = new Vector<T>(10, 10);
	}

	/**
	 * Adds an object to the storage data structure
	 * 
	 * @param e	Object to be added to the data structure	
	 * 
	 * @return	true/false value based on whether the object could be added
	 */
	
	@Override
	public boolean add( T e ) {
		int size = vector.size();
		if( size == 0 ) {
			return vector.add((T) e);
		}
		else {
			int i;
			for( i = 0; i < size; i++ ) {
				int low = i;
				
				if( e.compareTo(vector.get(low)) <= 0 ) {
					shiftRight(low);
					vector.set(low, (T) e);
					return true;
				}
				
			}
			if( i == size )
				return vector.add((T) e);
			
		}
		return false;
	}
	
	private void shiftRight( int index)
	{
		int size = vector.size();
		vector.add(size, vector.get(size - 1));
		for( int i = size-2; i >= index ; i-- ) {
			vector.set(i+1, vector.get(i));
		}

	}

	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
	
	@Override
	public void clear() {
		vector.clear();
	}

	
	/**
	 * Checks if the object is in the storage data structure
	 * 
	 * @param o	Object to be checked in the data structure	
	 * 
	 * @return	true/false value based on whether the object is there in the DS
	 */
	@Override
	public boolean contains(T o) {
		return vector.contains(o);
	}
	
	/**
	 * Checks if the data structure is empty
	 * 
	 * @return	true/false value based on whether the DS is empty
	 */

	@Override
	public boolean isEmpty() {
		return vector.isEmpty();
	}

	/**
	 * Removes an object from the storage data structure
	 * 
	 * @param o	Object to be removed from the data structure	
	 * 
	 * @return	true/false value based on whether the object could be removed
	 */
	@Override
	public boolean remove(T o) {
		return vector.remove(o);
	}

	/**
	 * Counts the objects in the storage data structure
	 * 
	 * @return	Number of elements in the DS
	 */
	@Override
	public int size() {
		return vector.size();
	}

	/**
	 * Returns the class name of the storage class
	 * 
	 * @return	name of the storage class
	 */	
	@Override
	public String getClassName() {
		return super.getClass().getName();
	}	

}
