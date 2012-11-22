import scala.math._
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
*/

object pe5 {

  def bruteForceSolver = {
    var value = 100
    var evenlyDivided = false
    while (!evenlyDivided) {
      evenlyDivided = divisbleByOneThroughTwenty_?(value)
      value += 1
    }
    value = value - 1
    println("value is " + value)
  }

  def divisbleByOneThroughTwenty_?(value:Int) = {
    var divisible_? = true
    var divisor = 2
    while (divisible_? && (divisor < 21)) {
      val divided = value / divisor
      val remainder = value - divided*divisor
      if (remainder == 0)
        divisible_? = divisible_? && true
      else
        divisible_? = divisible_? && false
      divisor += 1
    }
    divisible_?
  }
}
