import scala.math._

/*
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
*/

object pe9 {

  def solve = {
    var a = 0
    var b = 0
    for (i <- 1 to 999) {
      for (j <- 2 to 999) {
        if (equality(i,j)) {
          b = i
          a = j
        }
      }
    }
    val c = 1000 - a - b
    println("a = " + a)
    println("b = " + b)
    println("c = " + c)
    val product = a*b*c
    println(product)
  }

  def equality(a:Int, b:Int) = {
    (1000000 - 2000*a - 2000*b + 2*a*b) == 0
  }
}
