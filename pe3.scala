//find greatest prime factor of 600851475143
/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

/**
NOTES:

All prime numbers are odd except for 2

**/

object pe3 {

//iterative
  def solve(int:BigInt) = {
    val factors = List[Int]()
    val x = 3
    if (int % 2 == 0) factors :+ 2
    
    while (x < int) {
      if (int % x == 0) {
        if (isPrime(x))
          factors :+ x
      }
    }
    println(factors.sortWith(_ > _)(0))
  }

  def isPrime(x:Int) : Boolean = {
    val factors = List[Int]()
    for (i <- 1 to x) {
      if (i % 2 != 0)
        if (x % i == 0) 
          factors :+ i
    }
    (factors.length > 2) match {
      case true => false
      case false => true
    }
  }

  def stacked = {
    var n = 600851475143L; //not even, so 2 wont be a factor
    var factor = 3; 
    while( n > 1)
    {
      if (n % factor == 0)
      {
          n /= factor;
      } else
        factor += 2; //skip even numbrs
    }
    println(factor);
  }


  //TODO: Solve this again! Better!
}
