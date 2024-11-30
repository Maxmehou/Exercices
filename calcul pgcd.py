def calcul_pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

try:
    num1 = int(input("Entrez le premier nombre entier : "))
    num2 = int(input("Entrez le deuxième nombre entier : "))
    
    pgcd = calcul_pgcd(num1, num2)
    print(f"Le PGCD de {num1} et {num2} est : {pgcd}")
except ValueError:
    print("Veuillez entrer uniquement des nombres entiers valides.")
