package HomeWork3;
/*
 *  BackToTheFuture.java
 * 
 *  Version: BackToTheFuture.java, v 1.0 2017/12/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/12/09 10:10:05
 *      Initial Revision
 *      
 */

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/**
 * This program is implements the Hangman game
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class BackToTheFuture {	

	/**
	 * Main code that defines logic for the game
	 * 
	 * @param	inputFileName	Name of the file passed as an argument
	 * 
	 * @return					no returned value
	 */
	
	public void HangMan( String inputFileName ) {
				
		BackToTheFuture backToTheFuture = new BackToTheFuture();
		String continueGame = "no";
		String word;
		Scanner userInputScanner = new Scanner( System.in );
		StringBuffer guessedWord;
		
		System.out.println( "You are the You are the only player and " + 
		  "I name you Org. \nPlayer: Org" );
		
		//Read dictionary file and get all the words
		String[] dictionaryArray = 
				backToTheFuture.readFromDictionaryFile( inputFileName );
		
		do {
			
			int wrongGuessCount = 0;
			int bodyParts = 8;
			boolean win = false;
			String wrongGuesses = "";
			
			//Display complete hangman
			backToTheFuture.printHangman( bodyParts );
			
			//Read a random word from dictionaryArray
			word = backToTheFuture.readARandomWord( dictionaryArray );
			
			//Display initial wrong guesses
			System.out.print( wrongGuessCount + ": " );
			
			//Form the word with dots and display
			guessedWord = backToTheFuture.formTheGuessedWord( word, "", null );
			System.out.println( guessedWord );
					
			/*
			 * loop to continue till the user has guesses remaining
			 * and has not won
			 */
			while( wrongGuessCount < 8 && win == false ) {				
								
				//Read and validate the user input
				String guess = backToTheFuture.readAndValidateUserInput( 
						userInputScanner ).toLowerCase();
				
				//If the guess is not in the word
				if( word.indexOf( guess.charAt(0) ) < 0 ) {
					
					//To append wrong guesses to a string buffer
					wrongGuesses += wrongGuessCount == 0 ?  guess  : "," + 
							guess;
					++wrongGuessCount;
					--bodyParts;					
					
				}
				
				//Display body parts or current status of hangman
				backToTheFuture.printHangman( bodyParts );
				
				//Display current status of wrong guesses and guessedword
				System.out.print( wrongGuessCount + ": " );
				guessedWord = backToTheFuture.formTheGuessedWord( word, guess, 
						guessedWord );
				System.out.print( guessedWord );
				if( wrongGuessCount != 0 )
				 System.out.println("   Wrong guesses so far: "+wrongGuesses); 				
				
				
				//Check if guessedWord is equal to word
				if( word.equals( guessedWord.toString() ) ) {
					win = true;
					System.out.println( "You won!" );
				}				
				
			}
			System.out.println( "The word was: "+ word );
			System.out.print( "Do you want to continue (yes/no)? " );
			continueGame = userInputScanner.next().toLowerCase();
		} while( continueGame.equals( "yes" ) );
		
		userInputScanner.close();
	}
	
	/**
	 *  Prints the hangman based on the number of correct/incorrect guesses
	 *  
	 *  @return		no return value
	 */
	
	public void printHangman(int bodyParts) {
		String[][] hangman = {
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", "#", "#", " ", "#", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " "},
				{" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", "#", "#", " ", " ", " "},
				{"#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"},
				{"#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"}, 
				{"#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"}
		};
		
		/*
		 * Switch case to print hangman body parts
		 * based on number of wrong answers
		 */
		
		switch(bodyParts) {
			case 8: 
					for( int i = 0; i < hangman.length; i++ ) {
						for( int j = 0; j < hangman[0].length; j++ ) {
							System.out.print( hangman[i][j] );
						}
						System.out.println();
					}
					break;
			
			case 7:
				for( int i = 2; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
						System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
				
			case 6:
				for( int i = 3; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
						System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
			
			case 5:
				for( int i = 3; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
						if( ( i == 4 && j == 14 ) || ( i == 4 && j == 20 ) ) {
							System.out.print( " " );
						} else {
							System.out.print( hangman[i][j] );
						}
					}
					System.out.println();
				}
				break;
				
			case 4:
				for( int i = 7; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
							System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
				
			case 3:
				for( int i = 9; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
							System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
				
			case 2:
				for( int i = 10; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
							System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
				
			case 1:
				for( int i = 11; i < hangman.length; i++ ) {
					for( int j = 0; j < hangman[0].length; j++ ) {
							System.out.print( hangman[i][j] );
					}
					System.out.println();
				}
				break;
				
			case 0 : 
				break;
				
		}
	}
	
	/**
	 *  Reads from the dictionary file and returns all the word
	 *  
	 *  @return             all words from the dictionary file
	 */
	
	private String[] readFromDictionaryFile(String inputFileName) {
		
		String[] wordsArray = null;
		Scanner textFileScanner = new Scanner( 
				BackToTheFuture.class.getResourceAsStream( 
						inputFileName ) );
		ArrayList<String> wordsList = new ArrayList<String>();
			
		//Reading all the lines from the file into array list
		while( textFileScanner.hasNextLine() ) {
			String w = textFileScanner.next();
			wordsList.add(w);
		}
 		textFileScanner.close();
			
		//Convert words list to words array
		wordsArray = wordsList.toArray(new String[wordsList.size()]);		
		return wordsArray;
	}
	
	/**
	 *  This method reads a random word from the file dictionary array
	 *  for the player to start the game
	 *  
	 *  @param     dictionaryArray      array of words from dictionary.txt
	 *  
	 *  @return                         a random word from the dictionary array
	 *  
    */
	
	private String readARandomWord( String[] dictionaryArray ) {
		
		String randomWord = "";
		
		//Choose a random word from the array list of words
		if( dictionaryArray != null ) {
			int index = new Random().nextInt( dictionaryArray.length );
			randomWord = ( dictionaryArray[index] );	
		}		
		return randomWord;		
	}
	
	
	/**
	 *  This method forms the guessed word with dots or 
	 *  forms the dots if its the first time execution
	 * 
	 *  @param      word           the random word from dictionary
	 *  @param      guess          the character guessed by the user
	 *  @param      guessedWord    the guessed word with dots
	 *  
	 *  @return                    the guessed word with dots
	 *  
	 */
	
	private StringBuffer formTheGuessedWord( String word, String guess, 
			StringBuffer guessedWord ) {
		
		/*
		 * If the user guesses a character correctly,
		 * displays the guessed character and the remaining characters
		 * as dots
		 */
		if( guessedWord!= null && guessedWord.length() >= 1 ) { 
			for( int i = 0; i < word.length(); i++ ) {
				if( word.charAt(i) == guess.charAt(0) ) {
					guessedWord.setCharAt( i, guess.charAt( 0 )) ;
				}
			}
		}
		
		/*
		 * When the user starts the game it displays the dots corresponding
		 * to the characters in the word
		 */
		else {
			guessedWord = new StringBuffer( word.length() );
			for( int i = 0; i < word.length(); i++ ) {				
				guessedWord.append( "." );				
			}
		}
		return guessedWord;
	}
	
	/**
	 *  This method reads and validates the user input/word
	 *  
	 *  @param      userInputScanner    the scanner to read the input
	 *  
	 *  @return                         return the valid user input
	 *  
	 */
	
	private String readAndValidateUserInput( Scanner userInputScanner ) {
		System.out.println();
		
		//regex to validate user input
		while( !userInputScanner.hasNext( "[A-Za-z]{1}" ) ) {
			userInputScanner.next();
		}
		String guess = 	userInputScanner.next();
		return guess;
	}
	
	
	/**
	 * Calling function to other functions to implement
	 * the Hangman game
	 * 
	 * @param	args	    command line arguments( ignored )
	 * 
	 * @return			    no returned value
	 */
	
	public static void main( String[] args ) {
		BackToTheFuture backToTheFuture = new BackToTheFuture();
		String inputFileName = null;
		
		//to read the command line argument
		if (0 < args.length) {
			inputFileName = new String(args[0]);
		}
		backToTheFuture.HangMan(inputFileName);
	}
}
