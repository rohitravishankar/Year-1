import java.util.*;

public class TestString {
   final int MAX_ELEMENTS = 1000;
   final int MAX_COLLISION = 1;
   String allObjects[] = new String[ MAX_COLLISION * MAX_ELEMENTS];
   MyStorage<String> aStorage;
   long milliSeconds = 0;
   
   public TestString() {
   }
   public void start()	{
	milliSeconds = System.currentTimeMillis();
   }
   public void end()	{
	System.err.println("Time for all:	" + ( System.currentTimeMillis() - milliSeconds) );
   }
   public void init()	{
	int rennerle = 0;
	for ( int index = 0; index < MAX_COLLISION * MAX_ELEMENTS; index ++)		{
			allObjects[rennerle ++] = new String("" + 2 * index);
	}
   }
   public void print()	{
	for ( int index = 0; index < MAX_COLLISION * MAX_ELEMENTS; index ++)	
		System.out.println(index + ": " + allObjects[index]);
   }
   public void addTest()	{
	init();
	String o = null;
	boolean passed = true;
	for ( int index = 0; index < MAX_COLLISION * MAX_ELEMENTS; index ++)		{
		o = allObjects[index];
		if( ! aStorage.add( o ) ) {
			System.out.println("add of object at " + index + " failed ");
			System.out.println("\t" + o  );
			passed = false;
		}
	}
	if ( ! passed )
		System.out.println("add: for " +  aStorage.getClassName() + " failed.");
   }
   public void clearTest()	{
	   init();
	   boolean passed = true;
	   aStorage.clear();
	   int size = aStorage.size();
	   if( size > 0) {
		   passed = false;
	   }
	   if ( ! passed )
			System.out.println("clear: for " +  aStorage.getClassName() + " failed.");
   }
   public void containsTest()	{
	System.out.println(aStorage.contains(allObjects[0]));
   }
   public void isEmptyTest()	{
	System.out.println(aStorage.isEmpty());
   }
   
   public void removeTestObjectsWhichAreStored()	{
	init();
	String o = null;
	boolean passed = true;
	
	for ( int index = 0; index < MAX_COLLISION * MAX_ELEMENTS ; index ++ )	{
		o = allObjects[index];
		if  (! aStorage.remove( o ) )	{
			System.out.println("remove of existing object at " + index + " failed ");
			System.out.println("\t" + o  );
			passed = false;
		}

	}
	if (  aStorage.remove( o ) )	{
		System.out.println("remove of former existing object which has already been removed failed");
		System.out.println("\t" + o  );
		passed = false;
	}
	if ( ! passed )
		System.out.println("remove: for " +  aStorage.getClassName() + " failed.");
   }
   public void removeTestObjectsWhichAreNotStored()	{
	init();
	boolean passed = true;
	if  ( aStorage.remove( "this one does not exit in storage" ) )	{
		System.out.println("remove: of  none existing object did not fail");
		passed = false;
	}
	if ( ! passed )
		System.out.println("remove: for " +  aStorage.getClassName() + " failed.");
   }
   public void removeTest()	{
   	removeTestObjectsWhichAreStored();
	removeTestObjectsWhichAreNotStored();
   }
   public void sizeTest()	{
	System.out.println(aStorage.size() );
   }
   public void getClassNameTest()	{
	System.out.println(aStorage.getClassName() );
   }
   public <T> void testIt(MyStorage<T> aStorage)	{
	this.aStorage = (MyStorage<String>) aStorage;
	start();
	
	addTest();	
	removeTest();
	clearTest();
	isEmptyTest();
	sizeTest();
	getClassNameTest();

	end();
   }

   public static void main(String args[] )	{
	System.out.println("Hash Set :-");
	(new TestString()).testIt(new MyHashSet<String>());
	System.out.println("\nMy Fixed List :-");
	(new TestString()).testIt(new MyFixedList<String>());
	System.out.println("\nMy List :-");
	(new TestString()).testIt(new MyList<String>());
	System.out.println("\nMy Sorted List :-");
	(new TestInteger()).testIt(new MySortedList<String>());
	System.exit(0);
   }
}
