package HomeWork8;
/*
 *  Integral.java
 * 
 *  Version: Integral.java, v 1.0 2017/24/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/24/10 08:07:05
 *      Initial Revision
 *      
 */

/**
 * This class demonstrates the understanding of threads
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class Integral extends Thread{
	
	public final static double DELTA = 0.0001; 
	public final static double limit = 8.0;
	
	double greenDelta;
	double yellowDelta;
	double greenVolume;
	double yellowVolume;
	boolean volumeDifference;
	Integral threads[];
	
	
	public Integral() {
		
	}

	public Integral( double greenDelta , double yellowDelta ) {
		this.greenDelta = greenDelta;
		this.yellowDelta = yellowDelta;
	}
	
	
	/**
	 * Calculates f(x, y)
	 * 
	 * @param x	x value in the function
	 * @param y y value in the function 
	 * 
	 * @return     f(x, y) value
	 */
	public static double calculateFOfx( double x, double y ) {
		return ( Math.pow(x,2) + Math.pow(y, 2) );
	}
	
	/**
	 * Calculates the volume for a cuboid
	 * 
	 * @param dx 	The x value for the cuboid
	 * @param dy 	The y value for the cuboid
	 * @param z 		The z value for the cuboid 
	 * 
	 * @return       Volume of the cuboid
	 */
	private static double volumeCalc(double dx, double dy, double z) {
		return dx * dy * z;
	}
	
	/**
	 * Calculates the sum of volumes for the green and yellow cuboids
	 * 
	 * @param delta	The change for the x and y at which we calculate the function
	 * 
	 * @return       Sum of volumes of the green or yellow faces
	 */
	public static double greenOrYellowVolumeCalc( double delta ) {
		double z = 0;
		double volume = 0;
		for( double x = -4; x <= 4 ; x += delta ) {
			for ( double y = -4 ; y <= 4 ; y += delta ) {
				z = calculateFOfx(x, y);
				volume += volumeCalc( delta, delta, z);
			}
			
		}
		return volume;
	}
	
	
	/**
	 * Calculates the difference in volume for the green and yellow parts
	 * 
	 * @param greenVolume 	The volume of the green part
	 * @param yellowVolume	The volume of the yellow part
	 * 
	 * @return       		Checks if the difference in volume is less than DELTA
	 */
	public static boolean calculateVolumeDifference( double greenVolume, double yellowVolume ) {
		if( Math.abs( greenVolume - yellowVolume) <= DELTA ) {
			return true;
		}
		return false;
	}
	
	
	/**
	 * Calculates the difference in volume for the green and yellow parts
	 * 
	 * @param greenVolume 	The volume of the green part
	 * @param yellowVolume	The volume of the yellow part
	 * 
	 * @return       		Checks if the difference in volume is less than DELTA
	 */
	public void calculate( int numberOfThreads , double greenDivisions, double yellowDivisions ) {		
		
		threads = new Integral[numberOfThreads];
		
		for ( int i = 0; i < numberOfThreads; i++ ) {
			greenDelta = limit/greenDivisions;
			yellowDelta = limit/yellowDivisions;
			
			threads[i] = new Integral( greenDelta, yellowDelta );
			threads[i].start();
			
			greenDivisions += 100;
			yellowDivisions += 100; 
		}
		
		//Wait for all threads to finish
		for( int i = 0; i < threads.length; i++ ) {
			try{
				threads[i].join();
			}
			catch(InterruptedException e){
				System.out.println("Interrupted!");
			}
		}
		
		int flag = 0;
		for( int i = 0; i < threads.length; i++ ) {	
			 if ( threads[i].volumeDifference ) {
				    System.out.println("Green Volume : " + threads[i].greenVolume);
					System.out.println("Yellow Volume : " + threads[i].yellowVolume);
					System.out.format("Difference between volumes : %.10f " , (float)Math.abs( threads[i].greenVolume - threads[i].yellowVolume ));
					System.out.println("\nStep Size for green volume : " + threads[i].greenDelta );
					System.out.println("Step Size for yellow volume : " + threads[i].yellowDelta );	
					flag = 1;
					break;
			 }
			 
		}
		if( flag != 1 ) 
			calculate( numberOfThreads, greenDivisions, yellowDivisions );		
		
	}
	
	/**
	 * Calculates the yellow or green volumes and the difference in volume for the green and yellow parts
	 * for each thread
	 * 
	 * @return     No return value
	 */
	public void run() {
		greenVolume = greenOrYellowVolumeCalc( greenDelta );
		yellowVolume = greenOrYellowVolumeCalc( yellowDelta );
		volumeDifference = calculateVolumeDifference( greenVolume, yellowVolume );			
	}
}
