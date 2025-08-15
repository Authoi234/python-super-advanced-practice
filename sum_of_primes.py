def is_prime(n):
    """Check if a number is prime."""
    if n<=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    root = int(n**0.5) # n^0.5 = n^½ = √n , math.sqrt(n)

    for i in range(3, root+1, 2):
        if n%i == 0:
            return False
        
    return True
