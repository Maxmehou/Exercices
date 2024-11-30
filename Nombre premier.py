def np(n):
    if n < 2:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  


try:
    N = int(input("Entrez un nombre entier : "))
    
    
    if np(N):
        print(f"{N} est un nombre premier.")
    else:
        print(f"{N} n'est pas un nombre premier.")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")

