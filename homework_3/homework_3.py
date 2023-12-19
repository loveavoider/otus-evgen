import math;

# нахождение степени итеративно
def iterPow(num, p):
  res = 1
  for i in range(p):
    res *= num
  return res

# нахождение за log(n)
def logPow(num, p):
  if p == 0:
    return 1
  if p == 1:
    return num
  if p % 2 == 0:
    x = logPow(num, p / 2)
    return x * x
  else:
    return num * logPow(num, p-1)

# числа Фибоначчи
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

# числа Фибоначчи по формуле золотого сечения
def goldFib(n):
  f = (1 + math.sqrt(5)) / 2

  return abs(int(logPow(f, n) / math.sqrt(5) + 0.5))

def isPrime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

# счётчик простых чисел
def countPrime(num):
  count = 0
  for i in range(2, num):
    if isPrime(i):
      count += 1
  return count

# решето Эратосфена
def Er(n):
  r = [False] * n
  count = 0
  for i in range(2, len(r)):
    if not r[i]:
      count += 1
      for j in range(i, len(r), i):
        r[j] = True
  return count