package HomeWork2;
/* 
 * StringEx.java 
 * 
 * Version: StringEx.java, v 1.0 2017/28/08
 * 
 * Revisions: 
 *    Revision 1.0  2017/05/09 09:23:56  
 *    Initial revision 
 */

/**
 * This program displays twin primes in a given range.
 *
 * @author      Rohit Ravishankar
 * @author		Parinitha Nagaraja
 */

public class StringEx {
	
	//Stores concatenated list of all strings
	String allStrings;
	static String[] aText = {
			"Aab",
			"baB",
			"xxYYz",
			"avaJava"
	};
	
	/**
	 * To determine if a word is a palindrome or not
	 * 
	 * @param	palindrome	The string to be checked
	 * 						whether it is a palindrome or not
	 *            
	 * @return 				True/False based on whether the string is a
	 * 						palindrome or not
	 */
	
	private boolean isAPalindrome( String palindrome ) {
		if( palindrome.length() == 0 || palindrome.length() == 1) {
            return true; 
		} else if( palindrome.charAt( 0 ) == 
				palindrome.charAt( palindrome.length()-1 ) ) {
	            /* check the first and last character of String
	             *  if they are same then move forward to the next character from 
	             *  both sides
	             *  Recurse until you either find it to be a palindrome or no
	             */
	            return isAPalindrome(
	            		palindrome.substring( 1, palindrome.length()-1 ) );
		}
		return false;
	}
	
	/**
	 * To print all the palindromes in a given range
	 *
	 * @return		No return value
	 */
	
	public void printPalindromes() {
		
		//Iterating over the entire array of strings
		for(int i = 0; i < allStrings.length(); i++ ) {
			
			/*
			 * Iterating over the same array of strings and passing
			 * substring of the array to check whether it is a palindrome
			 * or not
			 */
			
			for( int j = i+1; j < allStrings.length(); j++ ) {
				
				/*
				 * slices the string and sends it as an argument to
				 * check whether it is  a palindrome or not
				 */
				String palin = allStrings.substring( i, j + 1 ) ;
				if( isAPalindrome( palin ) ) {
					System.out.println( allStrings.substring( i, j + 1 ) );
				}
			}
		}
	}
	
	/**
	 * To find all twin primes in a given range
	 *            
	 * @return 		To concatenate the array of strings
	 * 				to a single string
	 */
	
	public String concatenateStringArray() {
		StringBuffer concatenatedStrings = new StringBuffer();
		
		//To iterate and append all strings
		for ( int i = 0; i < aText.length; i++ ) {
			concatenatedStrings.append( aText[i] );
		}
		
		//To convert the entire string created to lower case
		allStrings =  concatenatedStrings.toString().toLowerCase();
		return allStrings;
	}
	
	/**
	 * Determines character distribution for an array
	 * of Strings
	 *            
	 * @return		Character distribution for characters between a-z
	 */
	
	public int[] characterDistribution() {
		
		//The array represents the number of alphabets
		int[] characterSet = new int[26];
		
		//Iterating over the array of strings
		for (int i = 0; i < aText.length; i++ ) {
			
			//Iterating over each string in the array
			for ( int j = 0; j < aText[i].length(); j++ ) {
				
				/*
				 * converting each string to lower case as 
				 * a & A are considered the same
				*/
				aText[i] = aText[i].toLowerCase();
				
				/*
				 * extract each character of the string and increment 
				 * the counter for that character
				 */
				char ch = aText[i].charAt(j);
				if( ch >= 'a' && ch <= 'z' ) {
					characterSet[ch - 'a']++;
				}
			}
		}
		return characterSet;
	}
	
	/**
	 * Calling function to other functions to facilitate
	 * finding the character distribution and all palindromic
	 * substrings
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */
	
	public static void main( String[] args ) {
		StringEx aStringEx = new StringEx();
		int[] characterSet = aStringEx.characterDistribution();
		for( int i = 0; i < characterSet.length; i++) {
			System.out.print( ( char ) ( i + 97) + " : " + characterSet[ i ] + "	" );
		}
		System.out.println();
		aStringEx.concatenateStringArray();
		aStringEx.printPalindromes();
	}

}
