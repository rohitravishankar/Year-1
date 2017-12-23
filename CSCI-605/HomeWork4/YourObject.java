/*
 *  YourObject.java
 * 
 *  Version: YourObject.java, v 1.0 2017/22/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/22/09 10:10:05
 *      Initial Revision
 *      
 */

import java.util.Random;

/**
 * This class demonstrates the implementation of Object
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */


public class YourObject {
	
	int hashcode;
	static Random randomInteger = new Random();
	int a;
	int b;
	
	//Default constructor
	public YourObject() {
		this.hashcode =  randomInteger.nextInt( 1000 ) + 13;
		this.a = 10;
		this.b = 20;
	}
	
	
	/**
	 * Code that creates a clone of an object
	 *
	 * @return		Cloned Object
	 */
	protected YourObject clone() {
		YourObject clonedObject = new YourObject();
		
		//Copy the contents of YourObject to clone
		clonedObject.a = this.a;
		clonedObject.b = this.b;
		return clonedObject;
	}
	
	/**
	 * Code that checks the equality of objects
	 *
	 * @returns true/false based on equality
	 */
	public boolean equals( Object obj ) {
		return ( this == obj );
	}
	
	/**
	 * Code generates hashcode
	 *
	 * @return	hashcode of an object
	 */
	public int hashCode() {
		return hashcode; 
	}
    
	/**
	 * Code that implements the toString method
	 *
	 * @return string representation of the object
	 */
	public String toString() {
		return getClass().getName() + "@" + 
				Integer.toHexString( hashCode() );	
	}
	
	/**
	 * Code that gets the class name of an object
	 *
	 * @return	Class name
	 */
	String  getClassName() {		
		return super.getClass().getName();	
	}
	
}

