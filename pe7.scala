import scala.math._

/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

object pe7 {

  def solve = {
    var primes = List[Int](2);
    val ithPrime = 10001
    var currentValue = 3

    while (primes.length < ithPrime) {
      if ((currentValue % 2) != 0) {
        var possible = true
        println("possible")
        for (prime <- primes) {
          if ((currentValue % prime) != 0)
            possible = possible && true
          else
            possible = possible && false
        }
        if (possible) {
          println("Adding " + currentValue)
          primes = primes :+ currentValue
        }
      }
      currentValue += 2
    }
    println(primes.last)
  }

}
