package HomeWork2;
class StringThing {
  public static void method(String id, String literal, String aNewString)       {
        System.out.println("method!" + id + ". " + (literal == aNewString ));
  }
  public static void main( String args[] ) {
        String aString = "123";
        String bString = "123";
        int number = 3;
        
        /*
         * 1. By L->R precedence, "a. " + "123" gets concatenated to
         * 	  produce "a. 123". 
         * 2. Since, this isn't equal to aString, false is returned
         * 
         * 1 string is generated as a result, i.e., "a. 123"
         */
        System.out.println("a.  " +     "123" == aString   );
        
        /*
         * 1. By precedence the operations within the parenthesis are
         * 	  evaluated first. 
         * 2. "12", a literal, is concatenated with an integer to produce a
         * 	  non literal "123".
         * 3. "123" is not equal to aString ("123"), a literal, as the address
         * 	  locations are different and hence returns false 
         * 
         * 2 strings are generated as a result, i.e.,
         *  -> "12" + number
         *  -> "b. " + result(false)
         */
        System.out.println("b.  " +   ( "12" + number == aString ) );
        
        /*
         * 1. By operator precedence, operands around "*" are evaluated first.
         * 2. Post  this, "c. " & aString string literal are concatenated by L->R
         * 	  precedence.
         * 3. This is further concatenated with the evaluated value.
         * 
         * 2 strings are generated as a result, i.e.,
         *  -> "c. " + aString
         *  -> ("c. " + aString ) + 23
         */
        System.out.println("c.  " +   aString  + 1 * 23 );
        
        /*
         * 1. By L->R precedence, the expression gets evaluated
         * 2. "d. " a string literal is concatenated with 123 to result in
         * 	  "d. 123" and which continues to the right to result in the output
         * 
         * 3 strings are generated as a result, i.e.,
         *  -> "d. " + 123
         *  -> ("d. " + 123) + number
         *  -> ("d. " + (123 + number)) + aString 
         */
        System.out.println("d.  " +   123 + number + aString  );
        
        /*
         * 1. By precedence, the operations within the parenthesis are
         * 	  evaluated first, to result in 126.
         * 2. By L->R precedence, "e. " a string literal is concatenated 
         * 	  with 126 to result in "e. 126" and which continues to the right
         *    to result in the output
         *   
         * 2 strings are generated as a result, i.e.,
         *  -> "e. " + (123 + number)
         *  -> ("e. " + (123 + number)) + aString  
         */
        System.out.println("e.  " +   ( 123 + number ) + aString   );
        
        /*
         * 1. By precedence, the operations within the parenthesis are
         * 	  evaluated first.
         * 2. By L->R precedence within the parenthesis, 123-2 is evaluated
         *    first which is concatenated with an empty string, then number, 
         *    and then further to aString
         * 3. This result is concatenated with "f. " and results in the output
         * 
         * 4 strings are generated as a result, i.e.,
         *  -> (123 - 2) + ""
         *  -> ((123 - 2) + "") + number
         *  -> (((123 - 2) + "") + number) + aString 
         *  -> "f. " + ((((123 - 2) + "") + number) + aString)
         */
        System.out.println("f.  " +   ( 123 - 2 + "" +  number + aString )  );
        
        /*
         * 1. By operator precedence, operands around "*" are evaluated first.
         * 2. Post  this, "g. ", "369" and aString string literal are 
         *    concatenated by L->R  precedence.
         *    
         * 2 string are generated as a result, i.e.,
         *  -> "g. " + (123 * number)
         *  -> ("g. " + (123 * number)) + aString  
         */
        System.out.println("g.  " +   123 * number + aString  );
        
        /*
         * 1. By operator precedence, operands around "/" are evaluated first to 41.
         * 2. Post  this, "h. ", number 41 and aString string literal are 
         *    concatenated by L->R  precedence. 
         *    
         * 2 string are generated as a result, i.e.,
         *  -> "h. " + (123 / number)
         *  -> ("h. " + (123 / number)) + aString      
         */
        System.out.println("h.  " +   123 / number + aString  );
        
        /*
         * 1. Insert parenthesis around the "-" operation
         * 2. By precedence, the operations within the parenthesis are
         * 	  evaluated first which results in 120.
         * 3. Post  this, "i. ", number 120 and aString string literal are 
         *    concatenated by L->R  precedence. 
         *    
         * 2 string are generated as a result, i.e.,
         *  -> "i. " + (123 - number)
         *  -> ("i. " + (123 - number)) + aString      
         */
        System.out.println("i.  " +  ( 123 - number )  + aString  );
        
        /*
         * 1. "x" + "yz" is evaluated to "xyz" string literal
         * 2. method is called on ("1", "xyz", "xyz") which results in true
         *    as 2 string literals with same value will point to the same address
         */
        method("1", "xyz", "x" + "yz");
        
        /*
         * 1. new String("x") + "yz" evaluates to a non literal "xyz"
         * 2. method is called on ("2", "xyz", "xyz") which results in false
         *    as of the arguments passed, 1 is a string literals and the other
         *    is a non literal
         */
        method("2", "xyz", new String("x") + "yz" );
        
        /*
         * 1. "x" + "y" + "z" is evaluated to "xyz" string literal
         * 2. method is called on ("3", "xyz", "xyz") which results in true
         *    as 2 string literals with same value will point to the same address
         */
        method("3", "xyz", "x" + "y" +"z");
        
        /*
         * 1. By operator precedence, operands around "*" are evaluated first.
         *    Post  this, "1", number 2 and 3, are concatenated by L->R  
         *    precedence.
         * 2. "1" + "2" + "3" is evaluated to "123" string literal
         * 3. method is called on ("4", "123", "123") which results in true
         *    as 2 string literals with same value will point to the same address
         */
        method("4", "1" + "2" + "3", "1" + 2 * 1 + 3);
        
        /*
         * 1. By L->R precedence, "1" , number 2 and 3, is evaluated to "123"
         *    string literal
         * 2. "1" + "2" + "3" is evaluated to "123" string literal
         * 3. method is called on ("5", "123", "123") which results in true
         *    as 2 string literals with same value will point to the same address
         */
        method("5", "1" + "2" + "3", "1" + 2 + 3);
        
        /*
         * 1. By precedence, the operations within the parenthesis are
         * 	  evaluated first.
         * 2. By L->R precedence, "1" , number 2 and 3, is evaluated to "123"
         *    string literal
         * 3. "1" + "2" + "3" is evaluated to "123" string literal
         * 4. method is called on ("6", "123", "123") which results in true
         *    as 2 string literals with same value will point to the same address
         */
        method("6", "1" + "2" + "3", "1" + (3 - 1)  + 3);
  }
}
