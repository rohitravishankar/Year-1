package HomeWork12;
/*
 *  PiEvenOddRMIInterface.java
 * 
 *  Version: PiEvenOddRMIInterface.java, v 1.0 2017/17/11
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/11 10:29:50
 *      Initial Revision
 *      
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * This program calculates the number of Even-Odd values of Pi using RMI
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 */

public interface PiEvenOddRMIInterface extends Remote {
	public void calculateEvenOddPiValues(char[] contentsOfFile) throws RemoteException;
	public long getOddCount() throws RemoteException;
	public long getEvenCount() throws RemoteException;
	public void resetStaticVariablesEvenAndOdd() throws RemoteException;
}
