def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))


# Tail Recursion
def factorial(x, result = 1):
  if (x == 1):
    return result
  return factorial(x - 1, result * x)

print(factorial(5, result = 1))