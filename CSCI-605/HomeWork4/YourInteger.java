/*
 *  YourInteger.java
 * 
 *  Version: YourInteger.java, v 1.0 2017/22/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/22/09 10:10:05
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the implementation of Integer class
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class YourInteger extends YourObject {
	static int MAX_VALUE;
	static int MIN_VALUE;
	static int SIZE;
	int value;
	
	//Default Constructor
	public YourInteger() {
		MAX_VALUE = 255;
		MIN_VALUE = 0;
		SIZE = 8;
	}
	
	//Parameterized constructor
	public YourInteger( YourString original ) {
		this.value = Integer.parseInt( original.toString(), 10 );
	}
	
	/**
	 * Code that compares 2 integer values
	 *
	 * @param anotherInteger	To check equality of current object value
	 * 						against this object's integer value
	 * 
	 * @returns				+,-,0 depending upon whether the integer 
	 * 						values are equal or not
	 */
	public int compareTo( YourInteger anotherInteger ) {
		 return ( this.value < anotherInteger.value ? 
				 -1 : ( this.value == anotherInteger.value ? 0 : 1 ) ); 
	}
	
	/**
	 * Code that checks the equality of 2 integer values
	 *
	 * @param	obj	To check equality of current object value
	 * 				against this object's integer value
	 * 
	 * @returns		true/false based on equality
	 */
	public boolean equals( Object obj ) {
		if( obj != null && obj.getClass() == YourInteger.class ) {
			return this.value == ( ( YourInteger )obj ).value;
		}
		return false;
	}
	
	
	/**
	 * Code that implements the toString method
	 *
	 * @return string representation of the object
	 */
	public String  toString() {
		return String.valueOf( this.value );
	}
	
	
}
