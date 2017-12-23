package HomeWork7;
/*
 *  GZipIOStreams.java
 * 
 *  Version: GZipIOStreams.java, v 1.0 2017/20/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/20/10 10:10:05
 *      Initial Revision
 *      
 */

import java.io.*;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * This class demonstrates the understanding of I/O
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class GZipIOStreams {


	/**
	 * Writes hashcode to a file
	 * 
	 * @param file	File to read from and write the hashcode to	
	 * 
	 * @exception	IOException if the File does not exist
	 * @exception	NoSuchAlgorithmException If a cryptographic algorithm is requested
	 * 										 but is not available in the environment
	 */
	
	public void writeToFile( File file ) throws IOException, NoSuchAlgorithmException {

		//To read the contents of the file
		FileInputStream fileInputStream = new FileInputStream( file );
		
		//To write contents into the file
		FileOutputStream fileOutputStream = new FileOutputStream( file, true );

		//Read all the file contents into an array of bytes
		byte[] fileByteArray = new byte[ ( int ) file.length() ];
		fileInputStream.read( fileByteArray );
		fileInputStream.close();

		//Retrieve the MD5 hash of the file contents
		String md5Hash = generateMd5Hash( fileByteArray );

		//Convert the hashcode returned to bytes
		byte[] md5HashByte = md5Hash.getBytes();

		//Append the hashcode to the end of the file
		fileOutputStream.write( md5HashByte );
		fileOutputStream.close();
	}

	
	/**
	 * Reads contents of a file and compares the hashcode of the contents to the hashcode in the file
	 * 
	 * @param file To read contents of file
	 * 
	 * @exception	IOException if the File does not exist
	 * @exception	HashcodeException if the Hashcodes do not match
	 * @exception	NoSuchAlgorithmException If a cryptographic algorithm is requested
	 * 										 but is not available in the environment
	 */
	public void readFromFile( File file ) throws IOException, NoSuchAlgorithmException, HashcodeException {
		
		//Get the path of the file
		String filePath = file.getAbsolutePath();
		
		//Read the contents of the file into until the hashcode starts (last 32 bits)
		RandomAccessFile randomFile = new RandomAccessFile( filePath, "r");
		int totalLength = ( int ) file.length();
		int fileContentLength = totalLength - 32;
		
		//Array of bytes to store the contents of the file
		byte[] fileContent = new byte[ fileContentLength ];
		randomFile.read( fileContent );
		
		//Calculate the hash code of the file contents
		String hash = generateMd5Hash( fileContent );
		
		long pos = fileContentLength;
		
		//Move the cursor to the position of the end of the contents, i.e., beginning of the hashcode
		randomFile.seek( pos );
		byte[] hashBytes = new byte[32];
		randomFile.read( hashBytes );
		String hashInFile = new String(hashBytes);
		
		//If the hashcode in the file and the hashcode of the contents do not match then throw an exception
		if ( ! compareHash( hash , hashInFile ) ) {
			throw new HashcodeException("Hashcode does not match!");
		}
		
		//Else display the hashcode
		else {
			System.out.println("Hash Code in File is " + hashInFile);
			System.out.println("Hash Code of the file " + hash);
		}
		randomFile.close();		
	}
	
	/**
	 * Compares hashcodes
	 * 
	 * @param hash		Hashcode of contents
	 * @param hashInFile	Hashcode in the file
	 * 
	 * @return 		true/false based on whether hashcodes are equal or not	
	 */

	private boolean compareHash( String hash, String hashInFile ) {
		return hash.equals( hashInFile );
	}

	/**
	 * Creates an MD5 hash
	 * 
	 * @param fileByteArray	Contents of the file
	 * 
	 * @return 				Hashcode of the contents	
	 * 
	 * @exception	IOException if the File does not exist
	 * @exception	NoSuchAlgorithmException If a cryptographic algorithm is requested
	 * 										 but is not available in the environment
	 */

	private String generateMd5Hash( byte[] fileByteArray ) throws NoSuchAlgorithmException, IOException {
		
		//Creates a hash code using using MD5 hashing
		MessageDigest md = MessageDigest.getInstance( "MD5" );
		md.update(fileByteArray);
		String md5Hash = ( new BigInteger(1, md.digest() ) ).toString(16);
		
		//Pad 0's to the beginning of the hash if the length is less than 32
		while( md5Hash.length() < 32 ){
			md5Hash = "0" + md5Hash;
		}
		return md5Hash;

	}

}