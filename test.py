# Programme de calculs mathématiques
# Déclaration des variables
a = 15
b = 7
c = 3.5

def func():
    """test de fonction"""
    return None

class Test:
    def __init__(self, x):
        self.key = x
    
    def header(self):
        return self.key

# Différents calculs
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
puissance = a ** 2
modulo = a % b
division_entiere = a // b
moyenne = (a + b + c) / 3
assert modulo == 1
if a == 12: assert modulo == 1
if x := 10 > 5:
    print(f"x est {x}")
# Affichage des résultats
a = 12
lst = []
for i in range(20):
    lst.append(i)
    x = (12+5j)
lst2 = [i for i in "Hey"]
print(f"Addition: {a} + {b} = {addition}")
print(f"Soustraction: {a} - {b} = {soustraction}")
print(f"Multiplication: {a} × {b} = {multiplication}")
print(f"Division: {a} ÷ {b} = {division:.2f}")
print(f"Puissance: {a}² = {puissance}")
print(f"Modulo: {a} % {b} = {modulo}")
print(f"Division entière: {a} // {b} = {division_entiere}")
print(f"Moyenne de {a}, {b}, {c} = {moyenne:.2f}")
print(a)
a: tuple[int] = complex(12)

var = Test();

print(var.header())

raise ValueError