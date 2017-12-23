package HomeWork11;
/*
 *  BackToTheFutureClient.java
 * 
 *  Version: BackToTheFutureClient.java, v 1.0 2017/17/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:51:09
 *      Initial Revision
 *      
 */

import java.io.*;
import java.net.Socket;

/**
 * This program is implements the Hangman game using Socket Programming
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class BackToTheFutureClient {
	
	/**
	 * Main code that defines client side logic
	 * 
	 * @param args	Command line arguments
	 * 
	 * @return		no returned value
	 */
	
	public static void main(String[] args) throws IOException, ClassNotFoundException {
		
		//Reading server information from command line arguments
		String serverIP = args[0];
		int port = Integer.parseInt(args[1]);

		// Printing out the port and IP of the server attempting to be connected
		System.out.println("Connecting to " + serverIP + " on port " + port);

		//Creating a new socket from the client end
		Socket client = new Socket(serverIP, port);
		System.out.println("Connected to " + client.getRemoteSocketAddress());

        // Output stream for sending the words to server 
		ObjectOutputStream objectOutputStream = new ObjectOutputStream( client.getOutputStream() );
		
		//Reading the information from the server
		ObjectInputStream objectInputStream = new ObjectInputStream( client.getInputStream() );
		
		// To print you are the only player and I name you org
		String s = (String) objectInputStream.readObject();
		System.out.println(s);	
		
		//To print the Hangman for the case until no inputs have been made
		s = (String) objectInputStream.readObject();
		System.out.println(s);	
		
		//To print the number of guesses and ...... corresponding to the characters not guessed
		s = (String) objectInputStream.readObject();
		System.out.println(s);	
 
		
		// Reading user input of letter
		BufferedReader stdIn = new BufferedReader( new InputStreamReader(System.in) );
		String userInput;
		
		//Keep reading the user input while the user doesn't want to continue the game
		while ( ( userInput = stdIn.readLine() ) != null ) {
			objectOutputStream.writeObject(userInput);
			if( userInput.equals("no") )
				break;
						
			//To display Hangman
			String hangman = (String) objectInputStream.readObject();
			System.out.println(hangman);
			
			//To display the wrong guess count and the .... for the wrong guesses
			String wrongGuessCount = (String) objectInputStream.readObject();
			System.out.print(wrongGuessCount);	
			
			//To display the wrong guessed words
			if( wrongGuessCount.charAt(0) != '0' ) {
				String wrongGuessedWord = (String) objectInputStream.readObject();
				System.out.print(wrongGuessedWord);
			}
			
			//If user exhausted all tries
			if(wrongGuessCount.charAt(0) == '8') {
				String continueGame = (String) objectInputStream.readObject();
				System.out.println(continueGame);
			}
			
			//If the user won the game before exhausting all attempts
			if( !wrongGuessCount.contains(".") ) {
				String wonGame = (String) objectInputStream.readObject();
				System.out.println(wonGame);
				String continueGame = (String) objectInputStream.readObject();
				System.out.println(continueGame);
			}
		}
		
		objectOutputStream.close();
		stdIn.close();
		client.close();
		objectInputStream.close();

	}
	

}
