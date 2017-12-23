package HomeWork12;
/*
 *  BackToTheFutureImpl.java
 * 
 *  Version: BackToTheFutureImpl.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/**
 * This program implements the Hangman Game using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class BackToTheFutureImpl extends UnicastRemoteObject implements BackToTheFutureInterface {

	private static final long serialVersionUID = 1L;


	public BackToTheFutureImpl() throws RemoteException {

	}

	
	/**
	 *  Prints the hangman based on the number of correct/incorrect guesses
	 *  
	 *  @param 	bodyParts		Number of remaining body parts
	 *  
	 *  @return					Hangman based on the number of body parts
	 */
	
	public String printHangman(int bodyParts) {
		StringBuffer stringBuff = new StringBuffer();
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
		switch (bodyParts) {
		case 8:
			for (int i = 0; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					// out.print( hangman[i][j] );
					stringBuff.append(hangman[i][j]);
				}
				// out.println();
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 7:
			for (int i = 2; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 6:
			for (int i = 3; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 5:
			for (int i = 3; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					if ((i == 4 && j == 14) || (i == 4 && j == 20)) {
						stringBuff.append(" ");
					} else {
						stringBuff.append(hangman[i][j]);
					}
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 4:
			for (int i = 7; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 3:
			for (int i = 9; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 2:
			for (int i = 10; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 1:
			for (int i = 11; i < hangman.length; i++) {
				for (int j = 0; j < hangman[0].length; j++) {
					stringBuff.append(hangman[i][j]);
				}
				stringBuff.append(System.lineSeparator());
			}
			break;

		case 0:
			break;

		}
		return stringBuff.toString();

	}

	/**
	 * This method forms the guessed word with dots or forms the dots if its the
	 * first time execution
	 * 
	 * @param word  the random word from dictionary
	 * 
	 * @param guess 			the character guessed by the user
	 * 
	 * @param guessedWord 	the guessed word with dots
	 * 
	 * @return 				the guessed word with dots
	 * 
	 */

	public StringBuffer formTheGuessedWord(String word, String guess, StringBuffer guessedWord) {
		if (guessedWord != null && guessedWord.length() >= 1) {
			for (int i = 0; i < word.length(); i++) {
				if (word.charAt(i) == guess.charAt(0)) {
					guessedWord.setCharAt(i, guess.charAt(0));
				}
			}
		} else {
			guessedWord = new StringBuffer(word.length());
			for (int i = 0; i < word.length(); i++) {
				guessedWord.append(".");
			}
		}
		return guessedWord;
	}


	/**
	 * This method reads a random word from the file dictionary array for the player
	 * to start the game
	 * 
	 * @return a random word from the dictionary array
	 * 
	 */

	public String readARandomWord() {

		String inputFileName = "dictionary.txt";
		String[] wordsArray = null;

		Scanner textFileScanner = new Scanner(BackToTheFutureClient.class.getResourceAsStream(inputFileName));
		ArrayList<String> wordsList = new ArrayList<String>();

		// Reading all the lines from the file into array list
		while (textFileScanner.hasNextLine()) {
			String w = textFileScanner.next();
			wordsList.add(w);
		}
		textFileScanner.close();

		// Convert words list to words array
		wordsArray = wordsList.toArray(new String[wordsList.size()]);


		String randomWord = "";

		// Choose a random word from the array list of words
		if (wordsArray != null) {
			int index = new Random().nextInt(wordsArray.length);
			randomWord = (wordsArray[index]);
		}
		return randomWord;
	}

}
