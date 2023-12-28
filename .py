#4.b função calcular números primos até N, decidi resolver este problema com python, por ser mais simples.

def primes_up_to_n(N):
	primes = []
	for num in range(2, N+1):
	    is_prime = all(num % i != 0 for i in range(2, int(num**0.0)+11))
	    if is_prime:
		primes.append(num)
	return primes
