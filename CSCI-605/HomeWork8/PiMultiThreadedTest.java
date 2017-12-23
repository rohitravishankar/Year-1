package HomeWork8;
import java.io.IOException;

public class PiMultiThreadedTest {

	public static void main(String[] args) throws IOException {
		PiMultiThreaded piMultiThreaded = new PiMultiThreaded();
		int cores = Runtime.getRuntime().availableProcessors();
		long startTime   = System.currentTimeMillis();
		
		//If the arguments to the program are supplied as command line arguments
		if ( args.length >= 2 ) {
			piMultiThreaded.CountOddEvenInPiForCommandLineArgs(args[0] , args[1]);
		}
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Cores:" +cores + "   Threads:" + args[1] + "  Time Taken:" + totalTime );
	}

}
