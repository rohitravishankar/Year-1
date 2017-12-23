package HomeWork12;
/*
 *  BackToTheFutureClient.java
 * 
 *  Version: BackToTheFutureClient.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.Naming;
import java.util.Scanner;


/**
 * This program implements the Hangman Game using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class BackToTheFutureClient {
	
	
	/**
	 * Main code that defines logic for the client side of the game
	 * 
	 * @param	args				Command line arguments
	 * 
	 * @return					no returned value
	 */
	
	public static void main( String args[] ) {
		try {
			
			BackToTheFutureInterface backToTheFuture = (BackToTheFutureInterface)Naming.lookup("//localhost:"+args[0]+"/BackToTheFuture");	
			BackToTheFutureClient backToTheFutureClient = new BackToTheFutureClient();
			
			String continueGame = "no";
			String word;
			Scanner userInputScanner = new Scanner( System.in );
			StringBuffer guessedWord;
			
			System.out.println( "You are the You are the only player and " + 
			  "I name you Org. \nPlayer: Org" );
			
			do {
				
				int wrongGuessCount = 0;
				int bodyParts = 8;
				boolean win = false;
				String wrongGuesses = "";
				
				//Display complete hangman
				System.out.println(backToTheFuture.printHangman( bodyParts ));
				
				//Read a random word from dictionaryArray
				word = backToTheFuture.readARandomWord();
				
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
					String guess = backToTheFutureClient.readAndValidateUserInput( 
							userInputScanner ).toLowerCase();
					
					//If the guess is not in the word
					if( word.indexOf( guess.charAt(0) ) < 0 ) {
						wrongGuesses += wrongGuessCount == 0 ?  guess  : "," + 
								guess;
						++wrongGuessCount;
						--bodyParts;					
						
					}
					
					//Display body parts or current status of hangman
					System.out.println(backToTheFuture.printHangman( bodyParts ));
					
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
		catch(Exception ex) {
			System.out.println("BackToTheFutureClient exception: " +
					ex.getMessage());
					ex.printStackTrace();
		}
		
		
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
		while( !userInputScanner.hasNext( "[A-Za-z]{1}" ) ) {
			userInputScanner.next();
		}
		String guess = 	userInputScanner.next();
		return guess;
	}
	
	

}
