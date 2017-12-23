package HomeWork13;
import java.util.ListIterator;

public class LinkedList<E> {
	Node<E> head;
	
	boolean add(E e) {
		if( e == null ) {
			return false;
		}
		Node<E> newNode = new Node<E>(e);
		newNode.link = head;
        head = newNode;
        return true;
	}
	
	boolean add(int index, E e) {
		if (index > size()) {
			System.out.println("The index cannot be greater than the size of the list");
			return false;
		}
		
		//Iterating to the index
		int count = 0;
		Node<E> temporaryPrevious = head;
		Node<E> temporaryNext = head;
		while( count != index) {
			temporaryPrevious = temporaryPrevious.link;
			temporaryNext = temporaryNext.link;
			count++;
		}
		temporaryNext = temporaryNext.link;
		
		Node<E> newNode = new Node<E>(e);
		temporaryPrevious.link = newNode;
		newNode.link = temporaryNext;
		return true; 
		
	}
	
	void clear() {
		Node<E> temporaryPrevious = head;
		Node<E> temporaryNext = head;
		while( temporaryNext != null ) {
			temporaryNext = temporaryNext.link;
			temporaryPrevious.link = null;
			temporaryPrevious = temporaryNext;
		}
		head = null;
	}

	int size() {
		int countOfElements = 0;
		Node<E> temporaryNode = head;
		while( temporaryNode != null) {
			temporaryNode = temporaryNode.link;
			countOfElements++;
		}
		return countOfElements;
	}
	
	boolean contains( Object o ) {
		Node<E> temporary = head;
		while( temporary != null ) {
			if( (temporary.data).equals(o) ) 
				return true;
			temporary = temporary.link;
		}
		return false;
	}
	
	E element() {
		return (E) head;
	}
	
	Object[] toArray() {
		int countOfElements = size();
		Object[] arrayOfElements = new Object[countOfElements];
		Node<E> temporary = head;
		int index = 0;
		while( temporary != null ) {
			arrayOfElements[index] = temporary.data;
			index++;
		}
		return arrayOfElements;
	}
	
//	ListIterator<E> listIterator(int index){
//		return null;
//	}
	
	void printList() {
		Node<E> temporary = head;
		while( temporary != null ) {
			System.out.print(temporary.data + "\t" );
			temporary = temporary.link;
		}
		System.out.println();
	}
}
