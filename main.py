import metoda_bisekcji as mb
import metoda_stycznych as ms
import funkcje as f

# - - - w metody - - -

print("Wybierz metode:\n"
      "1 - Metoda bisekcji\n"
      "2 - Metoda stycznych")

flaga = True

while flaga:
    w_metody = input("Wybierz numer odpowiedzi: ")
    
    if w_metody != "1" and w_metody != "2":
        print("Niepoprawny w. Wybierz 1 lub 2.")
    else:
        flaga = False


# - - - w funkcji - - -

print("\nWybierz funkcje:\n"
      "1 - Funkcja wielomianowa\n"
      "2 - Funkcja wykladnicza\n"
      "3 - Funkcja trygonometryczna\n"
      "4 - Funkcja zlozona")

flaga = True

while flaga:
    w_funkcja = input("Wybierz numer odpowiedzi: ")

    if w_funkcja not in ["1", "2", "3", "4"]:
        print("Wybierz cyfe z zakresu 1-4")
    else:
        flaga = False

# - - - Deklaracja listy - - -

lista = []
flaga = True
i = 0

if w_metody == "1":
    if w_funkcja == "1":
        no_correct_value = True
        while no_correct_value:
            try:
                stopien = int(input("\nPodaj stopien wielomianu: "))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe calkowita.")
        for i in range(stopien+1):
            lista.append(float(input("Podaj wspolczynnik o indeksie {}: ".format(i))))

    elif w_funkcja == "2":
        no_correct_value = True
        while no_correct_value:
            try:
                lista.append(float(input("Funkcja jest postaci: a * b^x + c. Podaj a: ")))
                lista.append(float(input("Podaj b: ")))
                lista.append(float(input("Podaj c: ")))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe zmiennoprzecinkowa.")

    elif w_funkcja == "3":
        no_correct_value = True
        while no_correct_value:
            try:
                flaga2 = True
                while flaga2:

                    lista.append(float(input("\nWybierz funcje trygonometryczna\n"
                                             "1 - sinus\n2 - cosinus\n3 - tg\n4 - ctg\n" + "Podaj numer: ")))
                    if lista[0] not in [1, 2, 3, 4]:
                        print("Podaj cyfre z zakresu 1-4")
                    else:
                        flaga2 = False

                lista.append(float(input("Funkcja jest postaci: a * f(b * x). Podaj a: ")))
                lista.append(float(input("Podaj b: ")))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe zmiennoprzecinkowa.")


# - - - w kryterium zatrzymania algorytmu - - -


flaga = True

while flaga:
    w_kryterium = input("\nWybierz kryterium zatrzymania algorytmu\n"
                        "1 - Spelnienie warunku nalozonego na dokladnosc\n"
                        "2 - Osiagniecie maksymalnej liczby iteracji\n"
                        "Wybierz numer odpowiedzi: ")
    if w_kryterium == "1":
        flaga2 = True
        while flaga2:
            w_wariant = input("\nWybierz sposob oszacowania wyniku\n"
                              "A - Wariant A\n"
                              "B - Wariant B\n"
                              "Wybierz litere: ")
            if w_wariant not in ["A", "B"]:
                print("Wybierz litere A lub B.")
            else:
                no_correct_value = True
                while no_correct_value:
                    try:
                        parametr = float(input("\nPodaj epsilon: "))
                        no_correct_value = False
                    except ValueError:
                        print("Nieprawidlowe dane. Podaj liczbe zmiennoprzecinkowa.")
                flaga2 = False
        flaga = False
    elif w_kryterium == "2":
        no_correct_value = True
        while no_correct_value:
            try:
                parametr = int(input("Podaj liczbe iteracji: "))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe calkowita.")
        w_wariant = "0"
        flaga = False
    else:
        print("Wybierz cyfe 1 lub 2.")

if w_metody == "1":
    flaga1 = True

    # - - - w poczatku i konca przedzialu dla metody bisekcji - - -
    while flaga1:
        no_correct_value = True
        while no_correct_value:
            try:
                w_poczatek = float(input("\nPodaj poczatek przedzialu: "))
                w_koniec = float(input("Podaj koniec przedzialu: "))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe zmiennoprzecinkowa.")

        if mb.sprawdz_przedzial(w_poczatek, w_koniec, w_funkcja, lista):
            wynik, iterator = mb.metoda_bisekcji(w_funkcja, w_wariant, parametr, w_poczatek, w_koniec, lista)
            flaga1 = False
        else:
            print("Podany przedzial nie spelnia warunkow zadania. Wartosci funkcji w podanych punktach musza miec "
                  "przeciwne znaki.")
elif w_metody == "2":
    flaga = True

    while flaga:
        no_correct_value = True
        while no_correct_value:
            try:
                w_poczatek = float(input("\nPodaj poczatek przedzialu: "))
                w_koniec = float(input("Podaj koniec przedzialu: "))
                no_correct_value = False
            except ValueError:
                print("Nieprawidlowe dane. Podaj liczbe zmiennoprzecinkowa.")

        if ms.sprawdz_przedzial(w_poczatek, w_koniec, w_funkcja):
            wynik, iterator = ms.metoda_stycznych(w_funkcja, w_wariant, parametr, w_poczatek, w_koniec)
            flaga = False
        else:
            print("Podany przedzial nie spelnia warunkow zadania. Wartosci funkcji w podanych punktach musza miec "
                  "przeciwne znaki oraz wartosc f'(a) != 0.")

print("Wynik to: {:.6f}\n".format(wynik))
print("Liczba iteracji to: " + str(iterator))

f.rysuj_wykres(w_metody, w_funkcja, w_poczatek, w_koniec, wynik, lista)
