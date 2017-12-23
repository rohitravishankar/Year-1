package HomeWork11;
/*
 *  PiEvenOddClient.java
 * 
 *  Version: PiEvenOddClient.java, v 1.0 2017/17/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:05:19
 *      Initial Revision
 *      
 */

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

/**
 * This program is calculates the number of Even-Odd values of Pi using Socket Programming
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class PiEvenOddClient {
	
	/**
	 * Main code that defines client side logic
	 * 
	 * @param args	Command line arguments
	 * 
	 * @return		no return value
	 */
	
	public static void main(String [] args) {
		
		//Read hostname of the server and the port for the connection
		String serverIP = args[0];
		int port = Integer.parseInt(args[1]);
		try {
			
			//Printing out the port and IP of the server attempting to be connected
			System.out.println( "Connecting to " + serverIP + " on port " + port );
			
			//Creating a socket connection to the server
			Socket client = new Socket( serverIP, port );
			System.out.println( "Connected to " + client.getRemoteSocketAddress() );
			
			//Get the name of the file from the user 
			Scanner scanner = new Scanner(System.in);
			System.out.print("Enter the path of the file: ");
			String fileName = scanner.next();
			scanner.close();
			
			//Copy contents to a character array
			char[] contentsOfFile = getCharacterArray( fileName );
			System.out.println();
			
			//Send the data to the server
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(client.getOutputStream());
            objectOutputStream.writeObject(String.valueOf(contentsOfFile));
			
			//Reading the response from the server
            ObjectInputStream objectInputStream = new ObjectInputStream(client.getInputStream());
            String output = (String) objectInputStream.readObject();
            System.out.println(output);
	         
			client.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * Returns character array of the file contents
	 * 
	 * @param fileName	file name for which we are creating the character array 
	 * 
	 * @return			no return value
	 */
	
	private static char[] getCharacterArray( String fileName ) throws IOException {
		
		//Open the file and read all the contents to a character array
		File file = new File( fileName );
		BufferedReader bufferedReader = new BufferedReader( new FileReader( file ) );
		char[] buffer = new char[(int) file.length()];
		while( bufferedReader.read(buffer) != -1 ) {
		}
		bufferedReader.close();
		return buffer;
	}

}
