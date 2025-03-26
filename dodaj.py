
import sys

def dodaj(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python modul_dodajacy.py <liczba1> <liczba2>")
        sys.exit(1)
    
    try:
        liczba1 = float(sys.argv[1])
        liczba2 = float(sys.argv[2])
        wynik = dodaj(liczba1, liczba2)
        print(f"Wynik: {wynik}")
    except ValueError:
        print("Błąd: Podaj poprawne liczby!")

