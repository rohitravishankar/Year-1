/*
 *  MyList.java
 * 
 *  Version: MyList.java, v 1.0 2017/04/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/04/10 10:10:05
 *      Initial Revision
 *      
 */

import java.util.Arrays;

/**
 * This class demonstrates the use of inheritance
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class MyList<T> implements MyStorage<T> {
	T[] myList;
	int minSize = 1000;
	int sizeOfArray; 

	public MyList() {
		this.myList = (T[]) new Object[minSize];
		size();
	}

	/**
	 * Adds an object to the storage data structure
	 * 
	 * @param e	Object to be added to the data structure	
	 * 
	 * @return	true/false value based on whether the object could be added
	 */
	
   // true if e could have been added
	public boolean add( T e ) {
		int positionToAdd = isCapacity();
		this.myList[positionToAdd] = e;
		size();
		return true;
	}

	/**
	 * Checks if the MyList has capacity to add new element
	 * and returns the position to add the element
	 * 
	 * @return	position to add the element
	 */
	public int isCapacity() {
		int positionToAdd = this.sizeOfArray;
		if( positionToAdd == 0 ) {
			return 0;
		}
		else if( this.myList[positionToAdd - 1] == null ) {
			return ( positionToAdd - 1);
		}
		else if( this.myList.length == positionToAdd  ) {
			int newSize = this.sizeOfArray + minSize;
			this.myList = Arrays.copyOf(this.myList, newSize);
			return positionToAdd;
		}
		else {
			return positionToAdd;
		}
	}

	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
	
   // all elements will be removed
	public void clear()  {
		//Garbage collection - create a new object
		this.myList = (T[]) new Object[minSize];
		size();
	}
	
	/**
	 * Checks if the object is in the storage data structure
	 * 
	 * @param o	Object to be checked in the data structure	
	 * 
	 * @return	true/false value based on whether the object is there in the DS
	 */
	
   // true if o is in storage
	public boolean contains( T o )    {
		for( int i = 0; i < this.sizeOfArray; i++ ) {
			if( this.myList[i] != null && this.myList[i].equals(o) ) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Checks if the data structure is empty
	 * 
	 * @return	true/false value based on whether the DS is empty
	 */
	
   // true if storage is empty
	public boolean isEmpty() {
		if( this.myList[0] == null ) {
			return true;
		}
		return false;
	}
	
	/**
	 * Removes an object from the storage data structure
	 * 
	 * @param o	Object to be removed from the data structure	
	 * 
	 * @return	true/false value based on whether the object could be removed
	 */
	
   // true if o could be removed from storage
	public boolean remove( T e ) {
		for( int i = 0; i < this.sizeOfArray; i++ ) {
			if( this.myList[i] != null ) {
				if( this.myList[i].equals( e ) ) {
					shiftArrayElements( i );
					size();
					return true;
				}
			}			
		}
		return false;
	}
	
	/**
	 * Counts the objects in the storage data structure
	 * 
	 * @return	Number of elements in the DS
	 */
	
   // # of elements in storage
	public int size() {
		int countOfElements = 0;
		for( int i = 0; i < this.myList.length; i++ ) {
			if( this.myList[i] != null ) {
				countOfElements++;
			} else {
				break;
			}
		}
		this.sizeOfArray = countOfElements;
		return this.sizeOfArray;
	}

	/**
	 * Shifts the elements in the MyList DS post remove operation
	 * 
	 * @param indexOfElementRemoved	Index of the element removed	
	 * 
	 * @return						None
	 */
	private void shiftArrayElements( int indexOfElementRemoved ) {
		//If the element to be removed is the last element in this.myList
		if( indexOfElementRemoved == ( this.sizeOfArray - 1 ) ) {
			this.myList[indexOfElementRemoved] = null;
		}
		else {
			int i = 0;
			for( i = indexOfElementRemoved; i < ( this.sizeOfArray - 1 ); i++ ) {
				this.myList[i] = this.myList[i+1];
			}
			//Accounting for the deletion at last position, i would already be incremented at the end of for loop 
			this.myList[i] = null;
		}
	}

	/**
	 * Returns the class name of the storage class
	 * 
	 * @return	name of the storage class
	 */
	
   // class name;
	public String getClassName() {
		return super.getClass().getName();
	}
}





