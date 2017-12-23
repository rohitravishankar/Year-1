/*
 *  MyStorage.java
 * 
 *  Version: MyStorage.java, v 1.0 2017/01/10
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
public abstract class  MyStorage {
	
	/**
	 * Adds an object to the storage data structure
	 * 
	 * @param e	Object to be added to the data structure	
	 * 
	 * @return	true/false value based on whether the object could be added
	 */
	
   // true if e could have been added
   public boolean add(Object e) {
	return true;
   }
   
	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
   
   // all elements will be removed
   public void clear()	{
   }
   
	/**
	 * Checks if the object is in the storage data structure
	 * 
	 * @param o	Object to be checked in the data structure	
	 * 
	 * @return	true/false value based on whether the object is there in the DS
	 */
   
   // true if o is in storage
   public boolean contains(Object o)	{
	return true;
   }
   
	/**
	 * Checks if the data structure is empty
	 * 
	 * @return	true/false value based on whether the DS is empty
	 */
   
   // true if storage is empty
   public boolean isEmpty()	{
	return true;
   }
   
	/**
	 * Removes an object from the storage data structure
	 * 
	 * @param o	Object to be removed from the data structure	
	 * 
	 * @return	true/false value based on whether the object could be removed
	 */
   
   // true if o could be removed from storage
   public boolean remove(Object o)	{
	return true;
   }
   
	/**
	 * Counts the objects in the storage data structure
	 * 
	 * @return	Number of elements in the DS
	 */
   
   // # of elements in storage
   public int size()	{
	return 0;
   }
   
	/**
	 * Returns the class name of the storage class
	 * 
	 * @return	name of the storage class
	 */
   
   // class name;
   public String getClassName() {
        return "MyStorage";
   }
}

