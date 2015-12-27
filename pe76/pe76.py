# break n_0 into two parts: leading container and remaining ones
# consider: take two 1's from the remainig ones and add them together and add to leading container# take one 1 from the remaining ones and add it to the leading container value



def euler_partition(n, k, partitions=None):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  else:
    n_minus = (n - 1/2 * k * (3*k - 1))
    p_minus = find_partitions(n - 1/2 * k * (3*k - 1))
    n_plus = (n - 1/2 * k * (3*k + 1))
    p_plus = find_partitions(n - 1/2 * k * (3*k + 1))
    return (-1)**(k + 1) * p_minus + p_plus

def find_partitions(n):
  number_of_partitions = 0
  for k in range(1, n + 1):
    number_of_partitions += euler_partition(n, k)
  return number_of_partitions
