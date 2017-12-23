package HomeWork3;
/*
 *  ConstantOrNot.java
 * 
 *  Version: ConstantOrNot.java, v 1.0 2017/13/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/13/09 15:10:03
 *      Initial Revision
 *      
 */

/**
 * This program is to understand final keyword
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

class ConstantOrNot {

	private final int aInt = 1;
	private final String aString = "abc";
	private       String bString = "abc";
	private final String[] aArray = new String[10];

	
	public void doTheJob() {
		
		/*
		 * an integer declared with final keyword cannot be modified
		 * once initialized
		 */
		aInt = 3;
		
		/*
		 * an string declared with final keyword cannot be modified
		 * once initialized
		 */
		aString = aString + "abc";
		
		/*
		 * an string declared with final keyword cannot be modified
		 * once initialized
		 */
		aString = aString;
		
		/*
		 * an array of strings declared with final keyword cannot be modified
		 * once initialized
		 */
		aArray = new String[10];
		
		bString = aString;
		bString = aString + "def";
		aArray[0] = "abc";	
	}

	public static void main( String args[] ) {
		new ConstantOrNot().doTheJob();
	}
}	