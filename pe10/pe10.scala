import scala.math._

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million. 
*/

object pe10 {

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

*/

  def solve = {
    val answer = (2L to 2000000).filter(isPrime).sum
    println(answer)
  }

  def isPrime(num:Long) = {
    !(2L to math.sqrt(num).toInt).exists(num % _ == 0 )
  }

  
}
