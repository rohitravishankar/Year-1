
/*
 *  Maze.java
 * 
 *  Version: Maze.java, v 1.0 2017/17/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/09 10:10:05
 *      Initial Revision
 *      
 */

import java.util.Scanner;
import java.util.Stack;

/**
 * This class demonstrates the Corn Maze problem
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class Maze {

	public char[][][] inputMaze;
	
	/**
	 *  To read the maze into memory
	 *  
	 *  @param	inputFileName	File name containing the maze
	 *  
	 *  @return					3-D maze 
	 *  
    */
	
	public char[][][] ReadMaze(String inputFileName) {

		//Scanner object to count the rows and columns in the file 
		Scanner rowReader = new Scanner( Maze.class.getResourceAsStream( 
				inputFileName ) );
		int levels = 1;
		int rows = 0;
		int columns = 0;
		while( rowReader.hasNext() ) {
			++rows;
			String input = rowReader.nextLine();
			
			//Number of columns remain same irrespective of the levels/rows
			if( columns == 0 ) {
				columns = input.length();
			}
			
			//Whenever "next level" is encountered increment levels by 1
			if( input.equals( "next level" ) ) {
				++levels;
			}
		}
		
		//Accounting for the 2 extra rows of "next level"
		rows = rows - ( levels - 1 );
		
		//The number of rows per level
		rows = rows/levels;
		
		//creates the 3-D array with the relevant parameters
		inputMaze = new char[levels][rows][columns];
		rowReader.close();

		//Reads the rows character by character and creates the matrix
		rowReader =  new Scanner( Maze.class.getResourceAsStream( 
				inputFileName ));
		while( rowReader.hasNext() ) {

			for ( int z = 0; z < levels ; z++ ) {

				for ( int x = 0; x < rows; x++ ) {
					if( rowReader.hasNext() ) {
						String line = rowReader.nextLine();	 
						if( line.equals("next level") ) {
							
							/*
							 * x has got incremented as next level is 
							 * detected as another row
							 */
							x = x-1 ; 
							continue;
						}
						for ( int y = 0; y < columns; y++ ) {	                		                	       			
							inputMaze[z][x][y] = line.charAt(y);
						}
					}
				}
			}
		}
		rowReader.close();		
		return inputMaze;
	}
	
	/**
	 *  This method prints the maze
	 *  
	 *  @param	maze		3-D array containing the maze
	 *  
	 *  @return			None
	 *  
    */

	public void printMaze(char[][][] inputMaze){
		for ( int z = 0; z < inputMaze.length; z++ ) {
			for ( int x = 0; x < inputMaze[z].length; x++ ) {
				for ( int y = 0; y < inputMaze[z][x].length; y++ ) {
					System.out.print(inputMaze[z][x][y]);
				}
				System.out.println();
			}
			System.out.println();
		}

	}
	
	/**
	 *  This method solves the maze
	 *  
	 *  @param	inputMaze		3-D array containing the maze
	 *  
	 *  @return			None
	 *  
    */
	
	public char[][][] solveMaze( char[][][] inputMaze ){

		Stack<Coordinates> stack = new Stack<>();
		
		//Z position for the second level is 1
		int startZPosition = 1;
		
		//X position for the second level is 0
		int startXPosition = 0;
		
		//Y position for the second level is 1
		int startYPosition = 1;

		int x = startXPosition, y = startYPosition, z = startZPosition;
		
		/*
		 * Direction the pointer is pointing to
		 * North = 1, South = 2, East = 3 & West = 4
		 */
		int currentDirection = 2;
		
		int numberOfRows = inputMaze[0].length;
		int countHashes = 0;
		

		for ( int i = 0; i < inputMaze[1][numberOfRows - 1].length; i++ ) {
			char ch = inputMaze[1][numberOfRows - 1][i];
			if ( ch == '#' ) {
				countHashes++;
			}
		}
		
		/*
		 * If the last row of the maze has only #'s then
		 * there is considered to be no exit to the maze
		 */
		if( countHashes == inputMaze[0][0].length ) {
			System.out.println("No solution");
		}
		else {
			
			/*
			 * The rows are checked till last row - 1
			 * to prevent an ArrayIndexOutOfBoundsException 
			 */
			while( x < (inputMaze[0].length-1) ) {
				
				/*
				 * For each of the cardinal directions, we check:-
				 * 1. If you can exit out from up, then exit
				 * 2. If you can turn right, turn right 
				 * 3. If you cannot turn right, move forward
				 * 4. If you cannot do either 1 or 2, turn left
				 * 5. If none of the other cases are possible
				 * 		turn back and go on the same path
				 */
				
				/*
				 * Stack Operation to check for traversed routes which
				 * aren't a part of the final solution
				 * 
				 * 1. Check if the stack is empty, if it is 
				 * 		push the traversed coordinate/node(element)
				 * 		onto the stack
				 * 
				 * 2. Else the stack has elements, get the element from the
				 * 		top of the stack
				 * 		2.1 If the element matches the element we are pushing onto
				 * 			the stack, pop the element off the stack and 
				 * 			change the traversed path having '~' to '.'
				 * 		2.2 Else push the new element onto the stack
				 */
				if( currentDirection == 2 ) {
					if ( inputMaze[z-1][x][y] == '.' ) {
						 inputMaze[z-1][x][y] = '~';
						 inputMaze[z][x][y] = '~';
						 break;
					}
					else if( inputMaze[z][x][y-1] == '.' ) {
							currentDirection = 4;
							inputMaze[z][x][y] = '~';
							if ( !stack.empty() ) {
								if( stack.peek().getX() == x && 
										stack.peek().getY() == y && 
										stack.peek().getZ() == z ) {
									stack.pop();
									inputMaze[z][x][y] = '.';
								} else {
									stack.push( new Coordinates( z, x, y ) );
								}
							}
							else {
								stack.push( new Coordinates( z, x, y) );
							}
							--y;
					}
					else if( inputMaze[z][x][y-1] == '#' &&
							inputMaze[z][x][y+1] == '#' && 
							inputMaze[z][x+1][y] != '#' ) {
						currentDirection = 2;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						++x;
					}
					else if( inputMaze[z][x][y-1] == '#' && 
							inputMaze[z][x+1][y] == '#' && 
							inputMaze[z][x][y+1] != '#' ) {
						currentDirection = 3;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						++y;
					}
					else {
						currentDirection = 1;
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						stack.pop();
						--x;
					}
				} 
				else if( currentDirection == 3 ) {
					if ( inputMaze[z-1][x][y] == '.' ) {
						 inputMaze[z-1][x][y] = '~';
						 inputMaze[z][x][y] = '~';
						 break;
					}
					else if( inputMaze[z][x+1][y] == '.' ) {
							currentDirection = 2;
							inputMaze[z][x][y] = '~';
							if ( !stack.empty() ) {
								if( stack.peek().getX() == x && 
										stack.peek().getY() == y && 
										stack.peek().getZ() == z ) {
									stack.pop();
									inputMaze[z][x][y] = '.';
								} else {
									stack.push( new Coordinates( z, x, y ) );
								}
							}
							else {
								stack.push( new Coordinates( z, x, y) );
							}
							++x;
					}
					else if( inputMaze[z][x+1][y] == '#' && 
							inputMaze[z][x-1][y] == '#' &&
							inputMaze[z][x][y+1] != '#' ) {
							currentDirection = 3;
							inputMaze[z][x][y] = '~';
							if ( !stack.empty() ) {
								if( stack.peek().getX() == x && 
										stack.peek().getY() == y && 
										stack.peek().getZ() == z ) {
									stack.pop();
									inputMaze[z][x][y] = '.';
								} else {
									stack.push( new Coordinates( z, x, y ) );
								}
							}
							else {
								stack.push( new Coordinates( z, x, y) );
							}
							++y;
		
					}
					else if( inputMaze[z][x+1][y] == '#' && 
							inputMaze[z][x][y+1] == '#'  &&
							inputMaze[z][x-1][y] != '#') {
						currentDirection = 1;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						--x;
					}
					else {
						currentDirection = 4;
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						stack.pop();
						--y;
					}
				} 
				else if( currentDirection == 1 ) {
					if ( inputMaze[z-1][x][y] == '.' ) {
						 inputMaze[z-1][x][y] = '~';
						 inputMaze[z][x][y] = '~';
						 break;
					}
					else if( inputMaze[z][x][y+1] == '.' ) {
						currentDirection = 3;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						++y;
					}
					else if(  inputMaze[z][x][y-1] == '#' && 
							inputMaze[z][x][y+1] == '#'  &&
							inputMaze[z][x-1][y] != '#') {
						currentDirection = 1;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						--x;
					}
					else if( inputMaze[z][x][y+1] == '#' && 
							inputMaze[z][x-1][y] == '#' &&
							inputMaze[z][x][y-1] != '#') {
						currentDirection = 4;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						--y;
					}
					else {
						currentDirection = 2;
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						stack.pop();
						++x;
					}
				}
				else {
					if ( inputMaze[z-1][x][y] == '.' ) {
						 inputMaze[z-1][x][y] = '~';
						 inputMaze[z][x][y] = '~';
						 break;
					}
					else if( inputMaze[z][x-1][y] == '.' ) {
						currentDirection = 1;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						--x;
					}
					else if( inputMaze[z][x+1][y] == '#' && 
							inputMaze[z][x-1][y] == '#' &&
							inputMaze[z][x][y-1] != '#') {
						currentDirection = 4;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						--y;
	
					}
					else if( inputMaze[z][x-1][y] == '#' && 
							inputMaze[z][x][y-1] == '#' &&
							inputMaze[z][x+1][y] != '#' ) {
						currentDirection = 2;
						inputMaze[z][x][y] = '~';
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						++x;
					}
					else {
						currentDirection = 3;
						if ( !stack.empty() ) {
							if(stack.peek().getX() == x && 
									stack.peek().getY() == y && 
									stack.peek().getZ() == z) {
								stack.pop();
								inputMaze[z][x][y] = '.';
							} else {
								stack.push( new Coordinates( z, x, y ) );
							}
						}
						else {
							stack.push( new Coordinates( z, x, y) );
						}
						stack.pop();
						++y;
					}
				}
			}
			
			//To mark the last element we left marking during our iteration
			inputMaze[z][x][y] = '~';
		}
		
		/*
		 * The stack operation removes an additional character
		 * while marking a loop. To account for that if the 
		 * element preceding & succeeding the current element
		 * are marked & the current element isn't, mark the
		 * current element 
		 * 
		 */
		for ( int k = 0; k < inputMaze.length; k++ ) {
			for ( int i = 0; i < inputMaze[0].length; i++ ) {
				for ( int j = 0; j < inputMaze[0][0].length; j++ ) {
					if( i+1 != inputMaze[0].length && j+1 != inputMaze[0][0].length) {
						if( inputMaze[k][i][j] == '.' && 
								inputMaze[k][i][j-1] == '~' &&
								inputMaze[k][i][j+1] == '~' ) {
							inputMaze[k][i][j] = '~';
						}
						if( inputMaze[k][i][j] == '.' && 
								inputMaze[k][i+1][j] == '~' &&
								inputMaze[k][i-1][j] == '~' ) {
							inputMaze[k][i][j] = '~';
						}
					}
				}
			}
		}

		return inputMaze;
	}

	/**
	 * Calling function to other functions to implement
	 * the Corn Maze game
	 * 
	 * @param	args	    command line arguments( ignored )
	 * 
	 * @return			no returned value
	 */
	
	public static void main( String[] args ) {
		Maze maze = new Maze();
		String inputFileName = null;
		if (0 < args.length) {
			inputFileName = new String(args[0]);
		}
		maze.inputMaze = maze.ReadMaze(inputFileName);
		System.out.println("Input Maze is ");
		maze.printMaze(maze.inputMaze);
		maze.solveMaze(maze.inputMaze);
		System.out.println("\nThe output maze is : \n");
		maze.printMaze(maze.inputMaze);
		System.out.println();
	}
}

