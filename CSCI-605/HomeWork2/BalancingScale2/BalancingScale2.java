package HomeWork2;
/* 
 * BalancingScale2.java 
 * 
 * Version: BalancingScale2.java, v 1.0 2017/06/09
 * 
 * Revisions: 
 * 	  Revision 2.0	2017/06/09 10:51:32
 *    Revision 1.0  2017/01/09 08:49:21  
 *    Initial revision 
 */

/**
 * This program checks whether weights can be balanced.  
 * If yes, the weights are printed
 *
 * @author		Rohit Ravishankar
 * @author		Parinitha Nagaraja
 */

public class BalancingScale2 {
	static int arrayOfWeights[] = { 1, 2, 5, 10, 10, 25, 25, 25, 50 };
	static boolean T[][];

	/**
	 * Determines whether the weight can be balanced or not
	 * 
	 * @param	weightToBeBalanced	To read the weight to be balanced
	 *            
	 * @return 						Whether the weight can be balanced as a
	 * 								true/false value
	 */
	
	public boolean canBeBalanced( int weightToBeBalanced ) {

		T = new boolean[arrayOfWeights.length + 1][weightToBeBalanced + 1];
		
		//if the weight to be measured is 0, marks all values as true
		for( int i = 0; i <= arrayOfWeights.length; i++ ) {
			T[i][0] = true;
		}

		//populating the 2D array based knowledge of previous variables
		for( int i = 1; i <= arrayOfWeights.length; i++ ) {
			for( int j = 1; j <= weightToBeBalanced; j++ ) {
				if( j - arrayOfWeights[i - 1] >= 0 ) {
					T[i][j] = T[i - 1][j] ||
							T[i - 1][j - arrayOfWeights[i - 1]];
				} else {
					T[i][j] = T[i - 1][j];
				}
			}
		}
		
		//returns the final true/false value after computation
		return T[arrayOfWeights.length][weightToBeBalanced];
	}
	
	/**
	 * Prints the weight if a solution exists
	 *            
	 * @return 			All the weights used to balance the
	 * 					particular weight
	 */

	public String printWeights() {
		StringBuffer sb = new StringBuffer();
		
		//flag variable is used to modify the column pointer 
		int flag = 0;
		
		/*copyOfColumn is used to store column value and modify during the 
		 * next iteration
		 */
		int copyOfColumn = 0;
		for( int i = T.length - 1; i >= 0; i-- ) {
			for( int j = T[0].length - 1; j >= 0; j-- ) {
				if( flag == 1 ) {
					j = copyOfColumn;
				}
				
				//edge case condition when T[0][j] is reached
				if( i - 1 >= 0 ) {
					if( T[i][j] == true && T[i - 1][j] == true) {
						break;
					} else {
						
						/* case when the value is true but isn't coming from
						 *  T[i-1][j]
						 */
						if( T[i][j] == true && 
								T[i - 1][j - arrayOfWeights[i - 1]] == true ) {
							
							//adds the weight to list of weights
							sb.append( arrayOfWeights[i - 1] + "g " );
							flag = 1;
							copyOfColumn = j - arrayOfWeights[i - 1];
							break;
						}
					}
				}
			}
		}
		return sb.toString();
	}
	
	/**
	 * Computes the total sum of weights in the set of weights
	 *            
	 * @return 		Total sum of weights
	 */
	
	public static int sumOfWeights() {
		int sum = 0;
		for( int j = 0; j < arrayOfWeights.length; j++ ) {
			sum += arrayOfWeights[j];
		}
		return sum;
	}
	
	/**
	 * Calling function to other functions to check whether weight can be
	 * balanced or not
	 * 
	 * @param	args		command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */

	public static void main(String args[]) {
		BalancingScale2 balancingScale = new BalancingScale2();
		
		//weight to be balance
		int weightToBeBalanced = 144;
		
		//Case to tackle when weight to be balance is 0
		if( balancingScale.canBeBalanced( weightToBeBalanced ) == true && 
				weightToBeBalanced == 0 ) {
			System.out.print( weightToBeBalanced + "g:	yes" + ";" );
			System.out.println( "\tused weights = empty set" );
		} 
		
		//Case to print the weights
		else if( balancingScale.canBeBalanced( weightToBeBalanced ) == true ) {
			System.out.print( weightToBeBalanced + "g:	yes" + ";" );
			System.out.println( "\tused weights = " + 
					balancingScale.printWeights() );
		}
		
		/* 
		 * Case when the weight to be balanced exceeds the total sum of
		 * weights available
		 */
		else if( balancingScale.canBeBalanced(weightToBeBalanced) == false
				&& weightToBeBalanced > sumOfWeights() ){
			System.out.print( weightToBeBalanced + "g:	no" );
		} 
		
		/*
		 * Case when the weight to be balanced cannot be readily balanced
		 * by the set of weights available
		 */
		else if( balancingScale.canBeBalanced(weightToBeBalanced) == false
				&& weightToBeBalanced < sumOfWeights() ) {
			int flag = 0;
			for( int i = 1; i <= ( sumOfWeights() - weightToBeBalanced ); i++ ) {
				if( balancingScale.canBeBalanced( weightToBeBalanced +
						i ) == true &&
						balancingScale.canBeBalanced(i) == true) {
					System.out.println("Weight to be added to " + 
							weightToBeBalanced + "g is : " +
							i + "g");
					System.out.print( (weightToBeBalanced + 
							i ) + "g:	yes" + ";" );
					balancingScale.canBeBalanced( weightToBeBalanced + i );
					System.out.println( "\tused weights = " + 
							balancingScale.printWeights() );
					flag = 1;
					break;
				}
			}
			if( flag == 0 ) {
				System.out.print( weightToBeBalanced + "g:	no" );
			}
		} else {
			
		}
	}
}