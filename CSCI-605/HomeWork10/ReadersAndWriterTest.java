package HomeWork10;
import java.io.IOException;

public class ReadersAndWriterTest {

	public static void main(String args[]) throws IOException {
		if (args.length >= 2) {
			ReadersAndWriter rw = new ReadersAndWriter();

			//Reading number of reader threads as a command line argument
			int numberOfReaders = Integer.parseInt( args[1] );
			
			rw.startProcess( args[0] , numberOfReaders);

		}

	}

}
