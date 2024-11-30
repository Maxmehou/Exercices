def derivée(a, b):
    D = f"f'(x) = {2 * a}x + {b}" if b != 0 else f"f'(x) = {2 * a}x"
    return D

def primitive(a, b, c):
    P = f"F(x) = {a/3}x^3 + {b/2}x^2 + {c}x + C"
    return P
try:
    a = float(input("Entrez le coefficient a de la fonction : "))
    b = float(input("Entrez le coefficient b de la fonction : "))
    c = float(input("Entrez le coefficient c de la fonction : "))

    D = derivée(a, b)
    print(f"Dérivée : {D}")
    
    P = primitive(a, b, c)
    print(f"Primitive : {P}")

except ValueError:
    print("Veuillez entrer des nombres valides.")
