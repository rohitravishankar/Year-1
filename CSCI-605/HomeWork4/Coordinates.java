/*
 *  Coordinates.java
 * 
 *  Version: Coordinates.java, v 1.0 2017/17/09
 *  
 *  Revisions:
 *      Revision 1.0 2017/17/09 10:10:05
 *      Initial Revision
 *      
 */
public class Coordinates {
	int x;
	int y;
	int z;
	
	public Coordinates(int z, int x, int y) {
		this.z = z;
		this.x = x;
		this.y = y;
	}
	
	/**
	 *  This method returns value of x coordinate
	 *  
	 * @return value of x
	 *  
    */
	public int getX() {
		return x;
	}
	
	/**
	 *  This method returns value of y coordinate
	 *  
	 * @return value of y
	 *  
    */
	public int getY() {
		return y;
	}
	
	/**
	 *  This method returns value of z coordinate
	 *  
	 * @return value of z
	 *  
    */
	public int getZ() {
		return z;
	}
	
}