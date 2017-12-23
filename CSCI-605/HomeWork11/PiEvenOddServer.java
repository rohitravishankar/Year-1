package HomeWork11;
/*
 *  PiEvenOddServer.java
 * 
 *  Version: PiEvenOddServer.java, v 1.0 2017/17/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:51:09
 *      Initial Revision
 *      
 */

import java.io.*;
import java.net.*;

/**
 * This program is calculates the number of Even-Odd values of Pi using Socket Programming
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public class PiEvenOddServer extends Thread{
	private static ServerSocket aServerSocket;
	static long evenCounter = 0;
	static long oddCounter = 0;

	public PiEvenOddServer() {

	}

	public PiEvenOddServer(int port) {
		try {
			aServerSocket = new ServerSocket(port);
			aServerSocket.setSoTimeout(10000000);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	/**
	 *  To open communication and start the execution
	 * 
	 * @return		no return value
	 */
	public void run() {
		try {

			System.out.println ("Listening on port: " + aServerSocket.getLocalPort());

			//Creating a socket to listen to the client
			Socket server = aServerSocket.accept();

			//Connection to client
			System.out.println("Connected to " + server.getRemoteSocketAddress());

			//Read the input stream from the client
            ObjectInputStream objectInputStream = new ObjectInputStream(server.getInputStream());
            String str = (String) objectInputStream.readObject();

			//Put the data from the input to a character array 
			char[] buffer = str.toCharArray();

			//For the character array calculate the number of even and odd values 
			for( int i = 0; i < buffer.length; i++) {
				countEvenOdd( buffer[i] );
			}

			String output = "even = " + evenCounter + "\nodd = " + oddCounter + "\nodd/even = " + (double) oddCounter/evenCounter + "\n";
			
			//Write to the output stream
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(server.getOutputStream());
            objectOutputStream.writeObject(output);

            server.close();
			aServerSocket.close();
		}  catch (SocketTimeoutException s) {
			System.out.println("Socket timed out!");
		} catch (Exception e) {

		}
	}
	
	/**
	 *  Calculates whether a character is an even or odd digit
	 * 
	 * @param	character	Checks whether this character is even or odd
	 * 
	 * @return				no return value
	 */
	private static void countEvenOdd(char character) {
		
		//Check if the character encountered is a digit or not
		if( Character.isDigit( character ) ) {
			int digit = Integer.parseInt(String.valueOf(character));
			if ( digit == 0 || digit % 2 == 0 )
				++evenCounter;
			else
				++oddCounter;
		}
	}

	/**
	 * Main function of the program that initiates execution
	 * 
	 * @param  args  	Command line arguments
	 * 
	 * @return			no return value
	 */
	public static void main(String [] args) {
		int port = Integer.parseInt(args[0]);
		try {
			PiEvenOddServer piEvenOddServer = new PiEvenOddServer(port);
			piEvenOddServer.run();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
