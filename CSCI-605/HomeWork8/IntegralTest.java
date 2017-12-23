package HomeWork8;
import java.io.IOException;

public class IntegralTest {

	public static void main(String[] args) throws IOException {
		Integral integralMultiThreaded = new Integral();
		
		int cores = Runtime.getRuntime().availableProcessors();
		long startTime   = System.currentTimeMillis();
		
		//If the arguments to the program are supplied as command line arguments
		if ( args.length >= 1 ) {
			int numberOfThreads = Integer.parseInt( args[0] );
			integralMultiThreaded.calculate( numberOfThreads, 8.0, 4.0 );
		}
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Cores:" +cores + "   Threads:" + args[0] + "  Time Taken:" + totalTime );
	}

}
