def is_prime(n):
    
    for i  in range(2,(int(n**0.5)+1)):
        if n%i==0:
            return False
        
    return True
    
    
def get_largest_prime(n):
    
    for i in range (2,int(n)+1):
        if is-prime(i):
            num = i
        

    return (num)    
