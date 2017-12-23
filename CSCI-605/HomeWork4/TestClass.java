/*
 *  TestClass.java
 * 
 *  Version: TestClass.java, v 1.0 2017/22/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/12/09 10:10:05
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the test cases for 
 * YourObject, YourString and YourInteger
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class TestClass {

	public static void main( String[] args ) {
		
		System.out.println("----------------------Test Cases for YourObject--------------------------------------");
		
		//Object Creation
		YourObject yourObject = new YourObject();
		YourObject yourObject2 = new YourObject();
		
		//ClassName
		System.out.println( "The class name is: " + 
				yourObject.getClassName() );
		
		//Object address
		System.out.println( "Your Object address : " + yourObject );
		System.out.println( "Your object's toString() value : " +
				yourObject.toString() );
		
		//Cloning 
		System.out.print( "Is yourObject != yourObject's clone : " );
		System.out.println( yourObject != yourObject.clone() );		
		System.out.print( "Is yourObject class = class of yourObject's clone : " );
		System.out.println( yourObject.clone().getClass() == 
				yourObject.getClass() );
		
		//Hash code
		System.out.println( "HashCode of YourObject : " + 
				yourObject.hashCode() );
		System.out.println( "HashCode of new YourObject : " +
				new YourObject().hashCode() );
		System.out.println( "HashCode of new YourObject2 : "+ 
				yourObject2.hashcode );
		System.out.println( "HashCode of YourObject : " + 
				yourObject.hashCode() );
		
		//Equals		
		System.out.println( "Are YourObject and yourObject2 equal: " +
				yourObject.equals( yourObject2 ) );
		System.out.println( "Is YourObject and YourObject equal: " +
				yourObject.equals( yourObject ) );		
		
		System.out.println("\n\n----------------------Test Cases for YourString--------------------------------------");
		
		//Your string Object
		YourString firstString = new YourString( "First String" );
		System.out.println( "First String: " + firstString );
		
		YourString secondString = new YourString( "Second String" );
		System.out.println( "Second String: " + secondString );
		
		YourString thirdString = new YourString( "First String" );
		YourString fourthString = new YourString("");
		
		//charAt
		char c = firstString.charAt( 2 );
		System.out.println( "The character at position 2 of firstString is " +
				c );
		
		//compareTo
		int compare = firstString.compareTo( secondString );
		System.out.println( "Comparison of firstString with SecondString: " + 
				compare );
		compare = firstString.compareTo( firstString );
		System.out.println( "Comparison of firstString with itself: " + 
				compare );
		
		//concat
		YourString concat = secondString.concat(firstString);
		System.out.println( "The concatenation of two strings: " + 
				concat );
		
		//equals
		System.out.println( "First string equals Second: " + 
				firstString.equals( secondString ) );
		System.out.println( "First string equals Third: " + 
				firstString.equals( thirdString ) );
		
		//toString
		System.out.println( "ToString of first sting is: " + 
				firstString.toString() );
		
		//isEmpty
		System.out.println( "Is FirstString empty: " + 
				firstString.isEmpty() );
		System.out.println( "Is Fourth empty: " + 
				fourthString.isEmpty() );
		
		System.out.println( "\n\n----------------------Test Cases for YourInteger--------------------------------------");
		
		//Creation of Integer
		YourString s1 = new YourString( "40" );
		YourInteger i1 = new YourInteger( s1 );
		System.out.println( "Integer value of first integer is: " + i1.value );
		
		YourString s2 = new YourString( "30" );
		YourInteger i2 = new YourInteger( s2 );
		
		//compareTo
		System.out.println( "Comparison of first with second integer " + 
				i1.compareTo( i2 ) );
		System.out.println( "Comparison of second with first integer " + 
				i2.compareTo( i1 ) );
		System.out.println( "Comparison of first integer with itself " + 
				i1.compareTo( i1 ) );
		
		//equals
		System.out.println( "Is integer 1 equal to integer 2: " + 
				i1.equals( i2 ) );				
		System.out.println( "Is integer 1 equal to itself: " + 
				i1.equals( i1 ) );
				
		
		//toString
		System.out.println( "Integer 1 toString is: " + i1.toString() );
		System.out.println("\n\n----------------------End------------------------------------------------------------");
		

	}

}
