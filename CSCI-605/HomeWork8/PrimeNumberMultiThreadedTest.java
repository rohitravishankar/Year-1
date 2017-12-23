package HomeWork8;

import java.io.IOException;

public class PrimeNumberMultiThreadedTest {

	public static void main(String[] args) throws IOException, InterruptedException {
		PrimeNumberMultiThreaded primeNumberMultiThreaded = new PrimeNumberMultiThreaded();
		int cores = Runtime.getRuntime().availableProcessors();
		long startTime = System.currentTimeMillis();		

		// If the arguments to the program are supplied as command line arguments
		if (args.length == 2) {
			primeNumberMultiThreaded.main(args[0], args[1]);
		}
		else {
			System.out.println("Usage: java PrimeNumberMultiThreadedTest <MAX> <numberOfThreads>");
		}
		
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Cores:" +cores + "   Threads:" + args[0] + "  Time Taken:" + totalTime );
	}

}

