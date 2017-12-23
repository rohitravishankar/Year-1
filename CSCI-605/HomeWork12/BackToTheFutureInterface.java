package HomeWork12;
/*
 *  BackToTheFutureInterface.java
 * 
 *  Version: BackToTheFutureInterface.java, v 1.0 2017/27/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.RemoteException;

/**
 * This program implements the Hangman Game using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public interface BackToTheFutureInterface extends java.rmi.Remote {
	String printHangman(int bodyParts) throws RemoteException;
	StringBuffer formTheGuessedWord(String word, String string, StringBuffer guessedWord) throws RemoteException;
	String readARandomWord()  throws RemoteException;
}
