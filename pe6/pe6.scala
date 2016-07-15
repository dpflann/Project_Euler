import scala.math._
import java.math.MathContext

/*
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

object pe6 {

  def solve = {
    
  val squareOfSum = pow(5050,2)
    var sumOfSquares = 0

    for (i <- 1 until 101) 
      sumOfSquares += pow(i,2).toInt

    val mc = new MathContext(512)
    val sq = BigDecimal(squareOfSum,mc)
    val sum = BigDecimal(sumOfSquares,mc)

    val difference = sq - sum
    println(squareOfSum)
    println(sumOfSquares)
    println(difference)
  }

}
