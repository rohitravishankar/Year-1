/*
 *  MyFixedList.java
 * 
 *  Version: MyFixedList.java, v 1.0 2017/01/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/01/10 10:10:05
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the use of inheritance
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class MyFixedList extends MyStorage {
	Object[] fixedList;
	public int LENGTH_OF_FIXED_LIST = 1000;
	
	public MyFixedList() {
		this.fixedList = new Object[LENGTH_OF_FIXED_LIST];
		for( int i = 0; i < this.fixedList.length; i++ ) {
			this.fixedList[i] = null;
		}
	}

	/**
	 * Adds an object to the storage data structure
	 * 
	 * @param e	Object to be added to the data structure	
	 * 
	 * @return	true/false value based on whether the object could be added
	 */
	
	// true if e could have been added
	public boolean add( Object e ) {
		//check if any element is null, add the string there 
		for( int i = 0; i < this.fixedList.length; i++ ) {
			if( this.fixedList[i] == null ) {
				this.fixedList[i] = e;
				return true;
			}			
		}		
		return false;
	}
	
	
	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
	// all elements will be removed
	public void clear()  {
		for( int i = 0; i < this.fixedList.length; i++ ) {
			this.fixedList[i] = null;
		}
	}
	
	/**
	 * Checks if the object is in the storage data structure
	 * 
	 * @param o	Object to be checked in the data structure	
	 * 
	 * @return	true/false value based on whether the object is there in the DS
	 */
	// true if o is in storage
	public boolean contains( Object o )    {
		for( int i = 0; i < this.fixedList.length; i++ ) {
			if( this.fixedList[i] != null && this.fixedList[i].equals(o) ) {
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
		int countNullPositions = 0;
		for( int i = 0; i < this.fixedList.length; i++ ) {
			if( this.fixedList[i] == null ) {
				++countNullPositions;
			}
		}
		if( countNullPositions == this.fixedList.length ) {
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
	public boolean remove( Object o )      {
		for( int i = 0; i < this.fixedList.length; i++ ) {
			if( this.fixedList[i] != null ) {
				if( this.fixedList[i].equals( o ) ) {
					this.fixedList[i] = null;
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
		for( int i = 0; i < this.fixedList.length; i++ ) {
			if( this.fixedList[i] != null ) {
				countOfElements++;
			}
		}
		return countOfElements;
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
