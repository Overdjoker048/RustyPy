#!/usr/bin/env python3
"""Calculatrice simple - 4 opérations de base."""

def calculer(a: float, b: float, op: str) -> float:
    """Effectue l'opération entre a et b."""
    assert op in ["+", "-", "*", "/"], "Opération invalide";
    if op == "+":
        return a + b;
    elif op == "-":
        return a - b;
    elif op == "*":
        return a * b;
    elif op == "/":
        assert b != 0, "Division par zéro";
        return a / b;


def main() -> None:
    """Point d'entrée principal du programme."""
    print("=== CALCULATRICE ===");
    
    # Saisie utilisateur
    a: float = float(input("Premier nombre: "));
    b: float = float(input("Deuxième nombre: "));
    op: str = input("Opération (+, -, *, /): ").strip();
    
    try:
        # Calcul et affichage
        resultat: float = calculer(a, b, op);
        print(f"Résultat: {a} {op} {b} = {resultat}");
        
    except AssertionError as e:
        print(f"Erreur: {e}");
    except ValueError:
        print("Erreur: Saisie invalide");
    except Exception:
        print("Erreur inattendue");


# Exécution du programme
if __name__ == "__main__":
    main();