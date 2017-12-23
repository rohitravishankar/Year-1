package HomeWork8;
/*
 *  Pi.java
 * 
 *  Version: Pi.java, v 1.0 2017/28/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/28/10 08:07:05
 *      Initial Revision
 *      
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.BufferedInputStream;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import javax.imageio.ImageIO;
import javax.swing.JFrame;

/**
 * This class demonstrates the understanding of threads
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class Pi extends JFrame implements Runnable {
	byte[] buffer;
	private final int LENGTH_OF_SQUARE = 3;
	private final int LENGTH = 330;
	private final int LENGTH_OF_WINDOW = LENGTH * LENGTH_OF_SQUARE;
	private BufferedImage theImage;
	private static BufferedImage finalImage;
	private String fileName = "output.png";
	Reader input;

	public Pi() {
		super("Pi");
		setBounds(100, 100, LENGTH_OF_WINDOW, LENGTH_OF_WINDOW);
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public Pi(byte[] buffer , BufferedImage theImage) {
		this();
		this.buffer = buffer;
		this.theImage = theImage;
	}


	/**
	 * Count even odd occurrences if command line arguments are specified
	 * 
	 * @param filePath	    File path to read pi value
	 * @param numOfThreads	Number of threads
	 *            
	 * 
	 * @return No value returned
	 */
	public void CountOddEvenInPiForCommandLineArgs(String filePath,
			String numOfThreads) throws IOException {
		File file = new File(filePath);
		FileInputStream fileInputStream = null;
		BufferedInputStream bis = null;
		int size = (int) file.length();
		int numberOfThreads = Integer.parseInt(numOfThreads);
		
		//Calculate the buffer size
		int bufferSize = size / numberOfThreads;
		
		//Create a buffer for each thread
		byte[] buffer = new byte[bufferSize];
		
		int width = getWidth();
		int height = getHeight();
		
		//Calculate the image height for each thread
		int heightForEach = ( height/numberOfThreads );
		
		finalImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		
		try {
			fileInputStream = new FileInputStream(filePath);
			bis = new BufferedInputStream(fileInputStream);
			Thread threads[] = new Thread[numberOfThreads];
			Pi piMultithread[] = new Pi[numberOfThreads];
			int counter = 0;
			while (bis.read(buffer) != -1 && counter < numberOfThreads) {
				
				//Create a thread
				theImage = new BufferedImage(width, heightForEach, BufferedImage.TYPE_INT_RGB);
				piMultithread[counter] =  new Pi(buffer , theImage );
				threads[counter] = new Thread(piMultithread[counter]);	
				
				//Start the thread
				threads[counter].start();				
				
				++counter;
				buffer = new byte[bufferSize];
			}

			//Wait for all the threads to finish
			for (int i = 0; i < threads.length; i++) {
				try {
					threads[i].join();
				} catch (InterruptedException e) {
					System.out.println("Interrupted!");
				}
			}
			
			//Draw the final image
			Graphics graphics = finalImage.createGraphics();
			int finalHeight = 0;
			for (int i = 0; i < threads.length; i++) {
				BufferedImage img = piMultithread[i].theImage;
				graphics.drawImage(img, 0, finalHeight, this);
				finalHeight += img.getHeight();
			}
			graphics.dispose();
			
			//Save the image to the output file
			saveImage( finalImage );

		}

		catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		}

		catch (IOException e) {
			System.out.println(e.getMessage());
		}

		finally {
			if (fileInputStream != null)
				fileInputStream.close();
			if (bis != null)
				bis.close();
		}

	}
	
	/**
	 * Paints a square red if the number is even
	 * else paints the square blue 
	 * 
	 * 
	 * @return No value returned
	 */
	public void run() {
		input = new InputStreamReader(new ByteArrayInputStream(buffer));
		int red = Color.RED.getRGB();
		int blue = Color.BLUE.getRGB();
		for ( int y = 0; y < theImage.getHeight() - 1; y += LENGTH_OF_SQUARE ) {
			for ( int x = 0; x < theImage.getWidth() - 1; x += LENGTH_OF_SQUARE ) {
				char digit = nextDigit();				
				fillSquare(x, y, digit % 2 == 0 ? red : blue);
			}
		}
		repaint();
	}
	
	/**
	 * Gets the next digit in the input stream
	 * 
	 * 
	 * @return next digit in the input stream
	 */
	public char nextDigit() {
		char buf[] = new char[1];
		try {
			input.read( buf );
			if (buf[0] == '.')
				input.read(buf);
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(0);
		}
		return buf[0];
	}

	/**
	 * Fills the square with red or blue in the appropriate coordinates
	 * 
	 * 
	 * @return next digit in the input stream
	 */
	public void fillSquare(int xOrig, int yOrig, int color) {
		for ( int x = 0; x < LENGTH_OF_SQUARE; x++)
			for ( int y = 0; y < LENGTH_OF_SQUARE; y++)
				theImage.setRGB(xOrig + x, yOrig + y, color);
	}

	/**
	 * Saves the image to the output file
	 * 
	 * 
	 * @return no return value
	 */
	public void saveImage(BufferedImage theImage) {
		try {
			String suffix = fileName.substring(1 + fileName.lastIndexOf("."));
			File outputfile = new File(suffix + "_" + fileName);
			ImageIO.write(theImage, suffix, outputfile);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	@Override
	public void paint(Graphics g) {
		g.drawImage(finalImage, 0, 0, this);
	}
	
}
