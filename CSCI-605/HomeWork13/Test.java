package HomeWork13;
public class Test {
	public static void main(String args[]) {
		LinkedList<Integer> linkedList = new LinkedList<Integer>();
		
		
		//Addition operation
		System.out.println("Addition operation");
		linkedList.add(5);
		linkedList.add(4);
		linkedList.add(2);
		linkedList.add(1);
		linkedList.printList();
		System.out.println();
		
		//Addition operation at an index
		System.out.println("Addition operation at an index");
		linkedList.add(1, 3);
		linkedList.printList();
		System.out.println();
		
		//Size of the list
		System.out.println("Size of the list : " + linkedList.size());
		System.out.println();
		
		//Contains
		System.out.println("Contains");
		System.out.println("Does the linked list contain 3 ? " + linkedList.contains(3));
		System.out.println();
		
		//Contains
		System.out.println("Element");
		System.out.println("Element : " + linkedList.element());
		System.out.println();
		
		//Clear Operation
		System.out.println("Clear operation");
		linkedList.clear();
		linkedList.printList();
		System.out.println();
		
	}
}
