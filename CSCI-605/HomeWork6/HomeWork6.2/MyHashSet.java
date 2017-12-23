/*
 *  MyHashSet.java
 * 
 *  Version: MyHashSet.java, v 1.0 2017/04/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/04/10 10:10:05
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the use of inheritance
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class  MyHashSet<T> implements MyStorage<T> {
	MyFixedList<T> myFixedList;
	
	public MyHashSet() {
		myFixedList = new MyFixedList<T>();
		for( int i = 0; i < myFixedList.fixedList.length; i++ ) {
			myFixedList.add( (T) new MyList<T>() ) ;
		}
	}
	
	/**
	 * Creates a hashcode for an object
	 * 
	 * @param 	o		Object to be added to the data structure whose hashcode must be created
	 * 
	 * @return	hash		Hashed value of the object
	 */
	
	private int getHashCode( T o ) {
		String stringValueOfObject = o.toString();
		int hash = 7;
		for( int i = 0; i < stringValueOfObject.length(); i++ ) {
		    hash = hash * 7 + stringValueOfObject.charAt( i );
		}
		return hash;
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
	   int hashCode = getHashCode( e );
	   int index = hashCode % myFixedList.size();
	   if( contains(e) ) {
		   return false;
	   } else {
		   ( ( MyList ) myFixedList.fixedList[index] ).add( e );
		   return true;
	   }
   }
   
	/**
	 * Removed all objects from the storage data structure
	 * 
	 * @return	None
	 */
  
  // all elements will be removed
   public void clear()	{
	   for( int i = 0; i < myFixedList.fixedList.length; i++ ) {
			   ( ( MyList ) myFixedList.fixedList[i] ).clear();
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
   public boolean contains( T o )	{
	   int hashCode = getHashCode(o);
	   int index = hashCode % myFixedList.size();
	   for( int i = 0; i < ( (MyList) myFixedList.fixedList[index]).myList.length; i++ ) {
		   if( ( ( MyList ) myFixedList.fixedList[index] ).myList[i] != null )  {
			   if( ( ( MyList ) myFixedList.fixedList[index] ).myList[i].equals( o ) ) {
				   return true;
			   }
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
   public boolean isEmpty()	{
	   int count = 0;
	   for( int i = 0; i < myFixedList.fixedList.length; i++ ) {
		  if( ( ( MyList ) myFixedList.fixedList[i] ).myList[0] == null) {
			  ++count;
		  }
	   }
	   if( count == myFixedList.fixedList.length ) {
		   return true;
	   } else {
		   return false;
	   }
   }
   
	/**
	 * Removes an object from the storage data structure
	 * 
	 * @param o	Object to be removed from the data structure	
	 * 
	 * @return	true/false value based on whether the object could be removed
	 */
  
  // true if o could be removed from storage
   public boolean remove( T o )	{
	   int hashCode = getHashCode(o);
	   int index = hashCode % myFixedList.size();
	   if( contains( o ) ) {
		   ( ( MyList ) myFixedList.fixedList[index] ).remove(o);
		   return true;
	   }
	   else {
		   return false;
	   }
   }
   
	/**
	 * Counts the objects in the storage data structure
	 * 
	 * @return	Number of elements in the DS
	 */
  
  // # of elements in storage
   public int size()	{
	   int count = 0;
	   for( int i = 0; i < myFixedList.fixedList.length; i++ ) {
		    count += ( ( MyList ) myFixedList.fixedList[i] ).size();
	   }
	   return count;
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

