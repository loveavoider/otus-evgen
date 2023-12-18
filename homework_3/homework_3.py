
def iter(num, p):
  res = 1
  for i in range(p):
    print(i)
    res *= num
  return res

# 0 1 1 2 3 5 8 13 21 
def fib(num):
  if num == 1:
    return 0
  
  prev = 0
  curr = 1
  for i in range(num-2):
    newPrev = curr
    curr += prev
    prev = newPrev
    
  return curr
    
def isPrime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def countPrime(num):
  count = 0
  for i in range(2, num):
    if isPrime(i):
      count += 1
  return count

print(countPrime(10000))