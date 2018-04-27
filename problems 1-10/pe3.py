# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Returns prime factors for num
def prime_facts(num):
  n = num
  facts = []
  for i in range(2, n + 1):
    if i * i > num:
      if n > 1: facts.append(n)
      break
    while(n % i == 0):
      # while n divisible by i
      facts.append(i)
      n = n / i
  return facts

hi_fact = max(prime_facts(600851475143))
print(hi_fact)