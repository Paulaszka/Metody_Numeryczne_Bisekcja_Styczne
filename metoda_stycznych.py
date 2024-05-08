import funkcje as f


def metoda_stycznych(w_funkcja, w_wariant, parametr, w_poczatek, w_koniec):
    if w_poczatek < w_koniec:
        a = w_poczatek
    else:
        a = w_koniec

    iterator = 0
    f_a = f.funkcja_s(w_funkcja, a)

    # - - - Kryterium sprawdzajace iteracje - - -
    if w_wariant == "0":
        flaga = True
        while iterator < parametr and flaga:
            if f.pochodna_s(w_funkcja, a) != 0:
                a = oblicz_dokladnosc(w_funkcja, a)
            else:
                flaga = False
            iterator += 1

    # - - - Wariant A - - -
    elif w_wariant == "A":
        flaga = True
        if f.pochodna_s(w_funkcja, a) != 0:
            a_1 = a
            a -= f.funkcja_s(w_funkcja, a) / f.pochodna_s(w_funkcja, a)
            iterator += 1
            while abs(a_1 - a) >= parametr and flaga:
                if f.pochodna_s(w_funkcja, a) != 0:
                    a_1 = a
                    a = oblicz_dokladnosc(w_funkcja, a)
                else:
                    flaga = False
                iterator += 1

    # - - - Wariant B - - -
    else:
        flaga = True
        while abs(f_a) >= parametr and flaga:
            if f.pochodna_s(w_funkcja, a) != 0:
                a = oblicz_dokladnosc(w_funkcja, a)
                f_a = f.funkcja_s(w_funkcja, a)
            else:
                flaga = False
            iterator += 1
    return a, iterator


def oblicz_dokladnosc(w_funkcja, a):
    a -= f.funkcja_s(w_funkcja, a) / f.pochodna_s(w_funkcja, a)
    return a


def sprawdz_przedzial(w_poczatek, w_koniec, w_funkcja):
    if f.funkcja_s(w_funkcja, w_poczatek) * f.funkcja_s(w_funkcja, w_koniec) < 0:
        if f.pochodna_s(w_funkcja, w_poczatek) != 0:
            return True
    return False
