import numpy as np
from matplotlib import pyplot as plt


def funkcja_b(rodzaj, x, lista):
    if rodzaj == "1":
        y = 0
        for i in range(len(lista)):
            y += lista[i] * x ** i
        return y
    elif rodzaj == "2":
        return lista[0] * pow(lista[1], x) + lista[2]
    elif rodzaj == "3":
        if lista[0] == 1:
            return lista[1] * np.sin(lista[2] * x)
        elif lista[0] == 2:
            return lista[1] * np.cos(lista[2] * x)
        elif lista[0] == 3:
            return lista[1] * (np.sin(lista[2] * x) / np.cos(lista[2] * x))
        else:
            return lista[1] * (np.cos(lista[2] * x) / np.sin(lista[2] * x))
    elif rodzaj == "4":
        return x**3 + np.sin(x) + np.exp(x)


def funkcja_s(rodzaj, x):
    if rodzaj == "1":
        return (2 * x + 5) * x - 3
    # 0 2 x=0,5
    elif rodzaj == "2":
        return pow(4, x) - 1
    # -1 1 x=0
    elif rodzaj == "3":
        return np.sin(x / 2)
    # 4 8 x=6.28
    elif rodzaj == "4":
        return x**3 + np.sin(x) + np.exp(x)
    # -2 2 x=-0.5


def pochodna_s(rodzaj, x):
    if rodzaj == "1":
        return 4 * x + 5
    elif rodzaj == "2":
        return pow(4, x) * np.log(4)
    elif rodzaj == "3":
        return 0.5 * np.cos(x / 2)
    elif rodzaj == "4":
        return 3*x**2 + np.cos(x) + np.exp(x)


def rysuj_wykres(w_metody, w_funkcja, w_poczatek, w_koniec, wynik, lista):
    x = np.linspace(w_poczatek, w_koniec, 400)
    if w_metody == "1":
        y = funkcja_b(w_funkcja, x, lista)
    else:
        y = funkcja_s(w_funkcja, x)

    plt.plot(x, y, color="magenta")
    plt.title('f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    # plt.xticks(range(0, 16))
    plt.scatter(wynik, 0, color="purple", marker='o', zorder=3)
    plt.show()
