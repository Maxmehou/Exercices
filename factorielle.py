def factorielle():
    try:
        n = int(input("Entrez un nombre entier : "))
        
        if n < 0:
            print("Le factoriel n'est pas défini pour les nombres négatifs.")
        else:
            F = 1
            for i in range(1, n + 1):
                F *= i
            
            print(f"Le factoriel de {n} est : {F}")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

factorielle()
