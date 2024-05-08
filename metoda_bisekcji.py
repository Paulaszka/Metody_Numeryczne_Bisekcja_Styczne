import funkcje as f


def metoda_bisekcji(w_funkcja, w_wariant, parametr, w_poczatek, w_koniec, lista):

    if w_poczatek < w_koniec:
        a = w_poczatek
        b = w_koniec
    else:
        a = w_koniec
        b = w_poczatek

    iterator = 0
    xi = (a + b) / 2
    f_xi = f.funkcja_b(w_funkcja,xi,lista)

# - - - Kryterium sprawdzajace iteracje - - -
    if w_wariant == "0":
        while iterator < parametr:
            xi, a, b = oblicz_dokladnosc("0", w_funkcja, a, b, xi, lista)
            iterator += 1

# - - - Wariant A - - -
    elif w_wariant == "A":
        xi_minus1 = (a + b) / 2
        xi, a, b = oblicz_dokladnosc("A", w_funkcja, a, b, xi_minus1, lista)
        iterator += 1
        while abs(xi - xi_minus1) >= parametr:
            xi_minus1 = xi
            xi, a, b = oblicz_dokladnosc("A", w_funkcja, a, b, xi, lista)
            iterator += 1

# - - - Wariant B - - -
    else:
        while abs(f_xi) >= parametr:
            iterator += 1
            xi, a, b = oblicz_dokladnosc("B", w_funkcja, a, b, xi, lista)
            f_xi = f.funkcja_b(w_funkcja, xi, lista)
    return xi, iterator


def oblicz_dokladnosc(kryterium, w_funkcja, a, b, xi, lista):

    f_xi = f.funkcja_b(w_funkcja, xi, lista)
    f_a = f.funkcja_b(w_funkcja, a, lista)

    if f_xi == 0:
        return (a + b) / 2, a, b
    elif f_xi * f_a < 0:
        b = xi
    else:
        a = xi
    return (a + b) / 2, a, b


def sprawdz_przedzial(w_poczatek, w_koniec, w_funkcja, lista):
    if f.funkcja_b(w_funkcja, w_poczatek, lista) * f.funkcja_b(w_funkcja, w_koniec, lista) < 0:
        return True
    else:
        return False