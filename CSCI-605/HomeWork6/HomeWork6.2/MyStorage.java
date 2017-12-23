/*
 *  MyStorage.java
 * 
 *  Version: MyStorage.java, v 1.0 2017/04/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/04/10 10:10:05
 *      Initial Revision
 *      
 */

/**
 * This file demonstrates the use of interface
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */
public interface MyStorage<T> {
	
	/**
	 * Adds an object to the storage data structure
	 * 
	 * @param o	Object to be added to the data structure	
	 * 
	 * @return	true/false value based on whether the object could be added
	 */
	
   // true if e could have been added
   public boolean add(T o); 
   
   
	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
   
   // all elements will be removed
   public void clear();
   
	/**
	 * Checks if the object is in the storage data structure
	 * 
	 * @param o	Object to be checked in the data structure	
	 * 
	 * @return	true/false value based on whether the object is there in the DS
	 */
   
   // true if o is in storage
   public boolean contains(T o);
   
	/**
	 * Checks if the data structure is empty
	 * 
	 * @return	true/false value based on whether the DS is empty
	 */
   
   // true if storage is empty
   public boolean isEmpty();
   
	/**
	 * Removes an object from the storage data structure
	 * 
	 * @param o	Object to be removed from the data structure	
	 * 
	 * @return	true/false value based on whether the object could be removed
	 */
   
   // true if o could be removed from storage
   public boolean remove(T o);
   
	/**
	 * Counts the objects in the storage data structure
	 * 
	 * @return	Number of elements in the DS
	 */
   
   // # of elements in storage
   public int size();
   
	/**
	 * Returns the class name of the storage class
	 * 
	 * @return	name of the storage class
	 */
   
   // class name;
   public String getClassName();
}

