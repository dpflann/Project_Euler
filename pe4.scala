import scala.math._

/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

object pe4 {

  def checkIfPalindrome(number:String) : Int = {
    if (number.reverse == number)
      return number.toInt
    else
      return 0
  }


  /* brute force product of 3 numbers is
  // (a*10^2 + b*10^1 + c*10^0) * (d*10^2 + e*10^1 + f*10^0) = X Y Z Z Y X
  // x*10^4 + y*10^3 + z*10^2 + y*10 + x

  a*d*10^4 + a*e*10^3 + a*f*10^2 + 
  b*d*10^3 + b*e*10^2 + b*f*10^1 +
  c*d*10^2 + c*e*10^1 + c*f

  value1 = a*10^2 + b*10^1 + c*10^0
  value2 = d*10^2 + e*10^1 + f*10^0*/

  def constructValue(a:Int, b:Int, c:Int, d:Int, e:Int, f:Int) : Int = {
    var currentMax = 0
    val number1 = (a*100 + b*10 + c)
    val number2 = (d*100 + e*10 + f)
    val product = number1 * number2       //(a*d*10000 + a*e*1000 + a*f*100 + b*d*1000 + b*e*100 + b*f*10 + c*d*100 + c*e*10 + c*f)

    
    val palindrome = checkIfPalindrome(product.toString)
    
    palindrome match {
      case 0 => 
      case _ => { println("(" + number1 + ", " + number2 + ")"); currentMax = math.max(currentMax, product) }
    }

    currentMax
  }

  def tryOutNumbers = {
    var max = 0
    //10^6 times -> 1,000,000
    // alternative: (100 - 999)*(100 - 999) -> 810,000 times
    for (a <- 0 until 10) 
      for (b <- 0 until 10)
        for (c <- 0 until 10)
          for (d <- 0 until 10)
            for (e <- 0 until 10)
              for (f <- 0 until 10) {
                val value = constructValue(a,b,c,d,e,f)
                value match {
                  case 0 =>
                  case _ => { max = math.max(value, max); println(max) }
                }
              }
    println("the max is : " + max)
  }


}

