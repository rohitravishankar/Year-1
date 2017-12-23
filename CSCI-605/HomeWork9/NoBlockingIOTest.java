package HomeWork9;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class NoBlockingIOTest {

	public static void main( String[] args ) throws IOException {		
		NoBlockingIO io = new NoBlockingIO( 
				new BufferedReader( 
						new InputStreamReader( 
								new FileInputStream( args[0] ) ) ) );
		io.read( args[0] );		
	}
}
