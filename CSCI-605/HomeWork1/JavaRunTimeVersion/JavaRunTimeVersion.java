package HomeWork1;
/* 
 * JavaRunTimeVersion.java 
 * 
 * Version: JavaRunTimeVersion.java, v 1.0 2017/28/08
 * 
 * Revisions: 
 *    Revision 1.0  2017/28/08 21:19:05  
 *    Initial revision 
 */

/**
 * This program displays the Java Runtime Version.
 *
 * @author      Rohit Ravishankar
 */

public class JavaRunTimeVersion {
	
	/**
	 * Calling function to other functions to facilitate printing the series
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */

	public static void main( String[] args ) {
		System.out.println( "Java Version: "
				+ System.getProperty( "java.version" ) );
	}
}

