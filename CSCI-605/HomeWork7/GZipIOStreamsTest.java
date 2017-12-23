package HomeWork7;
import java.io.File;
import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class GZipIOStreamsTest {

	/**
	 * Tests the GZipIOStreams class
	 * 
	 * @return 		No value returned
	 * 
	 * @exception	IOException if the File does not exist
	 * @exception	NoSuchAlgorithmException If a cryptographic algorithm is requested
	 * 										 but is not available in the environment
	 */
	public static void main(String[] args) throws NoSuchAlgorithmException, IOException, HashcodeException {
		GZipIOStreams gZipIOStreams = new GZipIOStreams();
		Scanner scanner = new Scanner( System.in );
		System.out.print("Enter file name/path to write : ");
		scanner = new Scanner( System.in );
		String filePath = scanner.next();
		File file = new File(filePath);
		gZipIOStreams.writeToFile( file );
		
		System.out.print("Enter file name/path to read : ");
		String readFilePath = scanner.next();
		File readFile = new File(readFilePath);
		gZipIOStreams.readFromFile( readFile );
		scanner.close();
	}

}
