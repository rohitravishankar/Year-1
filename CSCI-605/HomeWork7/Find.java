package HomeWork7;
/*
 *  Find.java
 * 
 *  Version: Find.java, v 1.0 2017/18/10
 *  
 *  Revisions:
 *      Revision 1.0 2017/18/10 08:07:05
 *      Initial Revision
 *      
 */

import java.io.File;
import java.util.Date;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * This class demonstrates the understanding of I/O
 * 
 * @author       Rohit Ravishankar
 * @author       Parinitha Nagaraja
 * 
 */

public class Find {
    String[] findCommand;
	static boolean isDisplayDate = false;
	static boolean isDisplayLength = false;
	static boolean isFile = false;
	static boolean isDirectory = false;
	static boolean isName = false;
	

	/**
	 * Writes hashcode to a file
	 * 
	 * @return No value returned
	 */
	public void patternMatchInput() {
		
		//Finds the length of the find command
		int length = findCommand.length;
		
		//Cases based on length of the find command
		switch(length) {
			case 5 :
				
				//If the date argument is supplied along with the other elements of the find command
				if( findCommand[4].equals("-date") ) {
					isDisplayDate = true;
					
					//find . -name <thisName> -date
					if( findCommand[2].equals("-name") ) {
						isName = true;
						executeCommand(findCommand[1]);
					} 
					
					//find . -type -f -date
					else if( findCommand[2].equals("-type") && findCommand[3].equals("-f") ) {
						isFile = true;
						executeCommand(findCommand[1]);
					} 
					
					//find . -type -d -date
					else if( findCommand[2].equals("-type") && findCommand[3].equals("-d") ) {
						isDirectory = true;
						executeCommand(findCommand[1]);
					}
					
				}
				
				//If the length argument is supplied along with the other elements of the find command
				else if( findCommand[4].equals("-length") ) {
					isDisplayLength = true;
					
					//find . -name <thisName> -length
					if( findCommand[2].equals("-name") ) {
						isName = true;
						executeCommand(findCommand[1]);
					} 
					
					//find . -type -f -length
					else if( findCommand[2].equals("-type") && findCommand[3].equals("-f") ) {
						isFile = true;
						executeCommand(findCommand[1]);
					} 
					
					//find . -type -d -length
					else if( findCommand[2].equals("-type") && findCommand[3].equals("-d") ) {
						isDirectory = true;
						executeCommand(findCommand[1]);
					}
				}
				break;
				
			case 4 :
				
				//If the type of files that need to be displayed are to be only files
				//find . -type -f
				if( findCommand[2].equals("-type") && findCommand[3].equals("-f") ) {
					isFile = true;
					executeCommand(findCommand[1]);
				}
				
				//If the type of files that need to be displayed are to be only directories
				//find . -type -d
				else if( findCommand[2].equals("-type") && findCommand[3].equals("-d") ) {
					isDirectory = true;
					executeCommand( findCommand[1] );
				}
				
				//If the type of files that need to be displayed match the name in the arguments
				//find . -name <thisName>
				else if( findCommand[2].equals("-name") ) {
					isName = true;
					executeCommand( findCommand[1] );
				}
				break;
			
			case 3 : 
				
				//find . -date
				if( findCommand[2].equals("-date") ) {
					isDisplayDate = true;
					executeCommand(findCommand[1]);
				}
				
				//find . -length
				else if( findCommand[2].equals("-length") ) {
					isDisplayLength = true;
					executeCommand(findCommand[1]);
				}
				break;
				
			case 2:
				
				//find .
				executeCommand( findCommand[1] );
				break;
			default :System.out.println("Incorrect input style\n "
					+ "Usage:  find  starting_directory [-name|-type (f|d)]|-date|-length]");
					break;
		}
		
	}
	
	/**
	 * Execute the command the user has entered
	 * 
	 * @return No value returned
	 */
    public void executeCommand( String path ) {
        File rootDirectory = new File( path );
        File[] listOfFiles = rootDirectory.listFiles();

        if (listOfFiles == null) {
        		return;
        }
        
        //Iterate through a list of files and print all the files recursively
        for ( File file : listOfFiles ) {
        	
        		//If the file encountered is a directory recursively display all the files
            if ( file.isDirectory() ) {
                executeCommand( file.getAbsolutePath() );
                if( !isFile ) {
                		displayOutput(file);
                }
            }
            else {
            		if( !isDirectory ) {
            			displayOutput(file);
            		}
            }
        }
    }
    
    
    /**
	 * Execute the command the user has entered
	 * 
	 * @param file To retrieve a file and display some information
	 * 
	 * @return No value returned
	 */
    private void displayOutput( File file ) {
    	    String filePath = file.getAbsolutePath();
    	    
    	    /*
    	     * All the if-else statements correspond to the switch cases 
    	     * of the patternMatchInput function
    	     */
    	    if( isDisplayDate ) {
    	    		if( isName && patterMatcher(file) ) {
    	    			System.out.println( filePath + "\t" + new Date (file.lastModified() * 1000 ) );
    	    		}
    	    		else if( isFile ) { 
    	    			System.out.println( filePath + "\t" + new Date (file.lastModified() * 1000 ) );
    	    		}
    	    		else if( isDirectory ) { 
    	    			System.out.println( filePath + "\t" + new Date (file.lastModified() * 1000 ) );
    	    		}
    	    		else if( !isDirectory && !isFile  && !isName ) {
    	    			System.out.println( filePath + "\t" + new Date (file.lastModified() * 1000 ) );
    	    		}
    	    }
    	    else if( isDisplayLength ) {
	    		if( isName &&  patterMatcher(file) ) {
	    			System.out.println( filePath + "\t" + file.length() );
	    		}
	    		else if( isFile ) { 
	    			System.out.println( filePath + "\t" + file.length() );
	    		}
	    		else if( isDirectory ) { 
	    			System.out.println( filePath + "\t" + file.length() );
	    		}
	    		else if( !isDirectory && !isFile  && !isName ) {
	    			System.out.println( filePath + "\t" + file.length() );
	    		}
	    }
    		else if( isName && patterMatcher(file) ) {
    			System.out.println( filePath );
    		}
    		else if( isFile ) {
    			System.out.println(filePath);
    		}
    		else if( isDirectory ) {
    			System.out.println(filePath);
    		}
    		else if( !isDirectory && !isName && !isFile && !isDisplayDate && !isDisplayLength ){
    			System.out.println( filePath );
    		}
    }
    
    /**
     * Match the pattern of the names of files
     * 
     * @param file File whose name needs to be checked
     * 
     * @return true/false if the filename matches or not 
     */
    
    private boolean patterMatcher( File file ) {
    	 String pattern = findCommand[3];
    	 if ( pattern.contains("*") )
    		 pattern = pattern.replace("*", ".*");
    	 if( pattern.contains("?") )
    		 pattern = pattern.replace("?", ".?");
    	 if( pattern.contains("+") )
    		 pattern = pattern.replace("+", ".+");
    	 Pattern p = Pattern.compile( pattern );
    	 Matcher matcher = p.matcher( file.getName() );
    	 boolean match = matcher.matches();
    	 return match;
    }
	
    /**
	 * Main function
	 * 
	 * @param args Command line args (ignored)
	 * 
	 * @return No value returned
	 */
	public static void main(String[] args) {
		Scanner scanner = null;
		Find find = new Find();
		System.out.print("Enter command : ");
		scanner = new Scanner(System.in);
		find.findCommand =  scanner.nextLine().split(" ");
		find.patternMatchInput();
		System.out.println();
		scanner.close();
	}

}
