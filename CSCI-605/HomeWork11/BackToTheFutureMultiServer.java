package HomeWork11;

/*
 *  BackToTheFutureMultiServer.java
 * 
 *  Version: BackToTheFutureMultiServer.java, v 1.0 2017/17/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:51:09
 *      Initial Revision
 *      
 */

import java.io.*;
import java.net.*;
import java.util.*;

/**
 * This program is implements the Hangman game using Socket Programming
 * 
 * @author Rohit Ravishankar
 * @author Parinitha Nagaraja
 */

public class BackToTheFutureMultiServer extends Thread {

	ServerSocket aServerSocket;
	int id = 0;
	private static String fileNameDictionary;

	public BackToTheFutureMultiServer() {
		aServerSocket = null;

	}

	public BackToTheFutureMultiServer(int port) {
		try {
			aServerSocket = new ServerSocket(port);
			aServerSocket.setSoTimeout(10000000);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public BackToTheFutureMultiServer(int port, int id) {
		this(port);
		this.id = id;
	}
	
	/**
	 * Opens ports for each client and puts it in the output stream
	 * 
	 * @return		no returned value
	 */
	public void listenToPort() {
		try {
			int id = 0;
			for (;;) {
				System.out.println("Wating for client to connect " + aServerSocket);
				Socket clientConnection = aServerSocket.accept();
				System.out.println("Somebody connected ... ");
				BackToTheFutureMultiServer aServer = new BackToTheFutureMultiServer(0, id++);
				aServer.start();

				//Displaying the port number which will be offered to the client
				System.out.println("offer ... " + aServer.getLocalPort());
				
				//Put the new port in the output stream
                PrintWriter out = new PrintWriter (clientConnection.getOutputStream (), true);
                out.println(aServer.getLocalPort());
                out.close();
                clientConnection.close();
			}
		} catch (Exception e) {
			System.out.println(e);
			e.printStackTrace();
		}
	}
	public int getLocalPort ()	{
        return aServerSocket.getLocalPort();
   }

	/**
	 * Main code that starts execution for each client
	 * 
	 * @return					no returned value
	 */
	public void run() {
		try {

			// Displays the port the server is listening on
			System.out.println("Listening on port: " + aServerSocket.getLocalPort());

			// Creating a socket to listen to the client
			Socket server = aServerSocket.accept();

			// Connection to client
			System.out.println("Connected to " + server.getRemoteSocketAddress());

			// Read the characters from client
			ObjectInputStream objectInputStream = new ObjectInputStream(server.getInputStream());

			// To send information to the client
			ObjectOutputStream objectOutputStream = new ObjectOutputStream(server.getOutputStream());

			// Calling the HangMan
			HangMan(fileNameDictionary, objectInputStream, objectOutputStream);
			
			server.close();

		} catch (Exception e) {

		}

	}

	/**
	 * Main code that defines logic for the game
	 * 
	 * @param	inputFileName		Name of the file passed as an argument
	 * @param	objectInputStream	Object input stream to read from the client
	 * @param	objectOutputStream	Object output stream to respond to the client
	 * 
	 * @return						no returned value
	 */

	public void HangMan(String inputFileName, ObjectInputStream objectInputStream,
			ObjectOutputStream objectOutputStream) throws IOException, ClassNotFoundException {

		BackToTheFutureMultiServer backToTheFuture = new BackToTheFutureMultiServer();
		String continueGame = "no";
		String word;

		StringBuffer guessedWord;

		objectOutputStream.writeObject("You are the You are the only player and " + "I name you Org. \nPlayer: Org");

		// Read dictionary file and get all the words
		String[] dictionaryArray = backToTheFuture.readFromDictionaryFile(inputFileName);

		do {

			int wrongGuessCount = 0;
			int bodyParts = 8;
			boolean win = false;
			String wrongGuesses = "";

			// Display complete hangman
			backToTheFuture.printHangman(bodyParts, objectOutputStream);

			// Read a random word from dictionaryArray
			word = backToTheFuture.readARandomWord(dictionaryArray);

			// Form the word with dots and display
			guessedWord = backToTheFuture.formTheGuessedWord(word, "", null);
			String guessedCountAndWord = wrongGuessCount + ": " + String.valueOf(guessedWord) + "\n";
			objectOutputStream.writeObject(guessedCountAndWord);

			/*
			 * loop to continue till the user has guesses remaining and has not won
			 */
			while (wrongGuessCount < 8 && win == false) {

				// Read and validate the user input
		 		String guess = backToTheFuture.readAndValidateUserInput(objectInputStream).toLowerCase();

				// If the guess is not in the word
				if (word.indexOf(guess.charAt(0)) < 0) {
					wrongGuesses += wrongGuessCount == 0 ? guess : "," + guess;
					++wrongGuessCount;
					--bodyParts;

				}

				// Display body parts or current status of hangman
				backToTheFuture.printHangman(bodyParts, objectOutputStream);

				// Display current status of wrong guesses and guessedword
				guessedWord = backToTheFuture.formTheGuessedWord(word, guess, guessedWord);
				objectOutputStream.writeObject(wrongGuessCount + ": " + String.valueOf(guessedWord));
				if (wrongGuessCount != 0) {
					String wrongGuessesString = "   Wrong guesses so far: " + wrongGuesses + "\n";
					objectOutputStream.writeObject(wrongGuessesString);
				}

				// Check if guessedWord is equal to word
				if (word.equals(guessedWord.toString())) {
					win = true;
					objectOutputStream.writeObject("You won!");
				}

			}
			objectOutputStream.writeObject("The word was: " + word + "\nDo you want to continue (yes/no)?\n");
			continueGame = (String) objectInputStream.readObject();
		} while (continueGame.equals("yes"));

		objectInputStream.close();
	}

	/**
	 * Reads from the dictionary file and returns all the word
	 * 
	 * @return all words from the dictionary file
	 */

	private String[] readFromDictionaryFile(String inputFileName) {

		String[] wordsArray = null;
		Scanner textFileScanner = new Scanner(BackToTheFutureMultiServer.class.getResourceAsStream(inputFileName));
		ArrayList<String> wordsList = new ArrayList<String>();

		// Reading all the lines from the file into array list
		while (textFileScanner.hasNextLine()) {
			String w = textFileScanner.next();
			wordsList.add(w);
		}
		textFileScanner.close();

		// Convert words list to words array
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

	private String readARandomWord(String[] dictionaryArray) {

		String randomWord = "";

		// Choose a random word from the array list of words
		if (dictionaryArray != null) {
			int index = new Random().nextInt(dictionaryArray.length);
			randomWord = (dictionaryArray[index]);
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

	private StringBuffer formTheGuessedWord(String word, String guess, StringBuffer guessedWord) {
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
	 * This method reads and validates the user input/word
	 *  
	 * @param      userInputScanner    the scanner to read the input
	 *  
	 * @return                         return the valid user input
	 * @throws IOException 
	 * @throws ClassNotFoundException 
	 *  
	 */

	private String readAndValidateUserInput(ObjectInputStream objectInputStream)
			throws ClassNotFoundException, IOException {
		System.out.println();
		String guess = null;
		guess = (String) objectInputStream.readObject();

		return guess;

	}

	/**
	 * Prints the hangman based on the number of correct/incorrect guesses
	 * 
	 * @return no return value
	 * @throws IOException
	 */

	public void printHangman(int bodyParts, ObjectOutputStream objectOutputStream) throws IOException {
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
					stringBuff.append(hangman[i][j]);
				}
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
		objectOutputStream.writeObject(String.valueOf(stringBuff));
	}

	

	/**
	 * Calling function to other functions to implement the Hangman game
	 * 
	 * @param args    command line arguments( ignored )
	 * 
	 * @return no returned value
	 */
	public static void main(String[] args) {
		int port = Integer.parseInt(args[0]);
		fileNameDictionary = args[1];
		try {
			BackToTheFutureMultiServer backToTheFutureServer = new BackToTheFutureMultiServer(port);
			backToTheFutureServer.listenToPort();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
