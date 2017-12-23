/*
 *  YourString.java
 * 
 *  Version: YourString.java, v 1.0 2017/22/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/22/09 10:10:05
 *      Initial Revision
 *      
 */

import java.util.Arrays;

/**
 * This class demonstrates the implementation of String
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class YourString extends YourObject{
	
	private char stringValue[];
	
	public YourString() {
		this.stringValue = new char[0];			
	}
	
	public YourString( String original ) {
		this.stringValue = original.toCharArray();		
	}	
	
	/**
	 * Code that returns a character at a position
	 *
	 * @param index	Position of character in the string
	 *
	 * @return		Returns character at a position
	 */	
	char charAt( int index ) {
		return this.stringValue[index];
	}
	
	/**
	 * Code that compares 2 strings
	 * 
	 * @param anotherString	String that this string must be compared against
	 *
	 * @return				+,-,0 depending upon whether the strings 
	 * 						are equal or not
	 */	
	int compareTo( YourString anotherString ) {
		
		//Store values of the length of the current string and anotherString
		int thisLen = this.stringValue.length;
		int anotherStringLen = anotherString.stringValue.length;
		
		//Finding the least length to iterate and compare
		int smallestLen = Math.min(thisLen, anotherStringLen);
		char[] thisChar = this.stringValue;
		char[] anotherStringChar = anotherString.stringValue;
		int i = 0;
		
		//Iterate and compare characters at the same position
		for( i = 0; i < smallestLen; i ++ ) {
			if( thisChar[i] != anotherStringChar[i] ) {
				return thisChar[i] - anotherStringChar[i];
			}
		}
		return 0;
	}
	
	/**
	 * Code that concatenates 2 strings
	 *
	 * @param str	String that this string must be concatenated with
	 *
	 * @return		concatenated strings
	 */
	
	YourString concat( YourString str ) {	
		int len = this.stringValue.length;
		
		/*
		 * Creates a copy of char array & store this string value 
		 * Also adds padding for the length of str
		 */
		char copyArr[] = Arrays.copyOf( this.stringValue, 
				len + str.toString().length() );
		
		//arraycopy(Object src, int srcPos, Object dest, int destPos,int length)
        System.arraycopy( str.stringValue, 0, 
        		copyArr, len,
        		str.toString().length() );
        
        YourString concat = new YourString();
        concat.stringValue = copyArr;
		return concat;
	}
	
	/**
	 * Code that checks for equality of 2 strings
	 * 
	 * @param	anObject		The object that this object must be checked against
	 *
	 * @return				true/false on whether the strings are equal or not
	 */
	public boolean equals( Object anObject ) {
		if( this == anObject )
			return true;
		
		//If this object has the same class as the obj object class
		if( anObject != null && anObject.getClass() == YourString.class ) {
			YourString str = ( YourString )anObject;
			for( int i = 0; i < str.stringValue.length; i++ ) {
				if( str.charAt(i) != this.charAt(i) ){
					return false;
				}				
			}
			return true;
		}
		return false;		
	}
	
	/**
	 * Code that returns string value of an object
	 *
	 * @return	string value of an object
	 */
	public String toString() {
		String newString = new String( this.stringValue );
		return newString;
	}
	
	/**
	 * Code that checks whether a string is empty or not
	 *
	 * @return	true/false value on whether the string is empty or not
	 */
	boolean  isEmpty() {
		return stringValue.length == 0;		
	}
	
}
