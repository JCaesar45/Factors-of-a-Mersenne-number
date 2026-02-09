function check_mersenne(p) {
    // Check if p is prime first
    if (!isPrime(p)) {
        return `M${p} = 2^${p}-1 is not prime (exponent not prime)`;
    }
    
    // Search for factor using the form q = 2*k*p + 1
    // where q must be 1 or 7 mod 8, q must be prime, and 2^p mod q = 1
    const limit = Math.sqrt(Math.pow(2, p) - 1);
    let k = 1;
    
    while (true) {
        const q = 2 * k * p + 1;
        
        // Stop if q exceeds sqrt(2^p - 1)
        if (q > limit) {
            break;
        }
        
        // q must be 1 or 7 mod 8
        if (q % 8 !== 1 && q % 8 !== 7) {
            k++;
            continue;
        }
        
        // q must be prime
        if (!isPrime(q)) {
            k++;
            continue;
        }
        
        // Check if 2^p mod q = 1 using modular exponentiation
        if (modPow(2, p, q) === 1) {
            return `M${p} = 2^${p}-1 is composite with factor ${q}`;
        }
        
        k++;
    }
    
    return `M${p} = 2^${p}-1 is prime`;
}

// Modular exponentiation: computes (base^exponent) % modulus efficiently
function modPow(base, exponent, modulus) {
    if (modulus === 1) return 0;
    
    let result = 1;
    base = base % modulus;
    
    while (exponent > 0) {
        // If exponent is odd, multiply base with result
        if (exponent & 1) {
            result = (result * base) % modulus;
        }
        
        // Exponent must be even now
        exponent = exponent >> 1; // Divide by 2
        base = (base * base) % modulus;
    }
    
    return result;
}

// Check if a number is prime
function isPrime(n) {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) return false;
    }
    
    return true;
}

// Test cases
console.log(check_mersenne(3));    // M3 = 2^3-1 is prime
console.log(check_mersenne(23));   // M23 = 2^23-1 is composite with factor 47
console.log(check_mersenne(929));  // M929 = 2^929-1 is composite with factor 13007
