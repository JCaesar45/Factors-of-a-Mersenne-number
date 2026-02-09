import math

def check_mersenne(p):
    """
    Check if Mersenne number M_p = 2^p - 1 is prime or find a factor.
    
    Args:
        p: The exponent (must be prime for M_p to potentially be prime)
    
    Returns:
        String indicating whether M_p is prime or composite with a factor
    """
    # Check if p is prime first
    if not is_prime(p):
        return f"M{p} = 2^{p}-1 is not prime (exponent not prime)"
    
    # Search for factor using the form q = 2*k*p + 1
    # where q must be 1 or 7 mod 8, q must be prime, and 2^p mod q = 1
    limit = math.isqrt(2 ** p - 1)
    k = 1
    
    while True:
        q = 2 * k * p + 1
        
        # Stop if q exceeds sqrt(2^p - 1)
        if q > limit:
            break
        
        # q must be 1 or 7 mod 8
        if q % 8 not in (1, 7):
            k += 1
            continue
        
        # q must be prime
        if not is_prime(q):
            k += 1
            continue
        
        # Check if 2^p mod q = 1 using modular exponentiation
        if mod_pow(2, p, q) == 1:
            return f"M{p} = 2^{p}-1 is composite with factor {q}"
        
        k += 1
    
    return f"M{p} = 2^{p}-1 is prime"


def mod_pow(base, exponent, modulus):
    """
    Modular exponentiation: computes (base^exponent) % modulus efficiently.
    Uses binary exponentiation (square-and-multiply) algorithm.
    """
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent & 1:
            result = (result * base) % modulus
        
        # Exponent must be even now
        exponent = exponent >> 1  # Divide by 2
        base = (base * base) % modulus
    
    return result


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Test cases
if __name__ == "__main__":
    print(check_mersenne(3))    # M3 = 2^3-1 is prime
    print(check_mersenne(23))   # M23 = 2^23-1 is composite with factor 47
    print(check_mersenne(929))  # M929 = 2^929-1 is composite with factor 13007
