import unittest
import metoda_bisekcji as mb
import metoda_stycznych as ms
import funkcje as f


class MyTestCase(unittest.TestCase):

    def test_something(self):
        lista_wielomian = [-3, 5, 2]
        lista = (mb.metoda_bisekcji("1", "A", 0.01, 0, 2, lista_wielomian))
        print("Wielomian, bisekcja, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", 0, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "A", 0.01, 0, 2))
        print("Wielomian, styczne, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", 0, 2, lista[0], lista_wielomian)

        lista = (mb.metoda_bisekcji("1", "B", 0.01, 0, 2, lista_wielomian))
        print("Wielomian, bisekcja, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", 0, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "B", 0.01, 0, 2))
        print("Wielomian, styczne, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", 0, 2, lista[0], lista_wielomian)

        lista = (mb.metoda_bisekcji("1", "0", 10, 0, 2, lista_wielomian))
        print("Wielomian, bisekcja, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", 0, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "0", 10, 0, 2))
        print("Wielomian, styczne, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", 0, 2, lista[0], lista_wielomian)

        #  - - - - - - - - - - - - - - - - - - - - - - -

        lista_wykladnicza = [1, 4, -1]
        lista = (mb.metoda_bisekcji("2", "A", 0.01, -1, 1, lista_wykladnicza))
        print("Wykladnicza, bisekcja, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "2", -1, 1, lista[0], lista_wykladnicza)

        lista = (ms.metoda_stycznych("2", "A", 0.01, -1, 1))
        print("Wykladnicza, styczne, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "2", -1, 1, lista[0], lista_wykladnicza)

        lista = (mb.metoda_bisekcji("2", "B", 0.01, -1, 1, lista_wykladnicza))
        print("Wykladnicza, bisekcja, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "2", -1, 1, lista[0], lista_wykladnicza)

        lista = (ms.metoda_stycznych("2", "B", 0.01, -1, 1))
        print("Wykladnicza, styczne, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "2", -1, 1, lista[0], lista_wykladnicza)

        lista = (mb.metoda_bisekcji("2", "0", 10, -1, 1, lista_wykladnicza))
        print("Wykladnicza, bisekcja, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "2", -1, 1, lista[0], lista_wykladnicza)

        lista = (ms.metoda_stycznych("2", "0", 10, -1, 1))
        print("Wykladnicza, styczne, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "2", -1, 1, lista[0], lista_wykladnicza)

        #  - - - - - - - - - - - - - - - - - - - - - - - -

        lista_trygonometryczna = [1, 1, 0.5]
        lista = (mb.metoda_bisekcji("3", "A", 0.01, 4, 8, lista_trygonometryczna))
        print("Tryg, bisekcja, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "3", 4, 8, lista[0], lista_trygonometryczna)

        lista = (ms.metoda_stycznych("3", "A", 0.01, 4, 8))
        print("Tryg, styczne, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "3", 4, 8, lista[0], lista_trygonometryczna)

        lista = (mb.metoda_bisekcji("3", "B", 0.01, 4, 8, lista_trygonometryczna))
        print("Tryg, bisekcja, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "3", 4, 8, lista[0], lista_trygonometryczna)

        lista = (ms.metoda_stycznych("3", "B", 0.01, 4, 8))
        print("Tryg, styczne, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "3", 4, 8, lista[0], lista_trygonometryczna)

        lista = (mb.metoda_bisekcji("3", "0", 10, 4, 8, lista_trygonometryczna))
        print("Tryg, bisekcja, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "3", 4, 8, lista[0], lista_trygonometryczna)

        lista = (ms.metoda_stycznych("3", "0", 10, 4, 8))
        print("Tryg, styczne, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "3", 4, 8, lista[0], lista_trygonometryczna)

        #  - - - - - - - - - - - - - - - - - - - - - - -

        lista_zlozona = [0]
        lista = (mb.metoda_bisekcji("4", "A", 0.01, -2, 2, lista_zlozona))
        print("Złożona, bisekcja, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "4", -2, 2, lista[0], lista_zlozona)

        lista = (ms.metoda_stycznych("4", "A", 0.01, -2, 2))
        print("Złożona, styczne, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "4", -2, 2, lista[0], lista_zlozona)

        lista = (mb.metoda_bisekcji("4", "B", 0.01, -2, 2, lista_zlozona))
        print("Złożona, bisekcja, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "4", -2, 2, lista[0], lista_zlozona)

        lista = (ms.metoda_stycznych("4", "B", 0.01, -2, 2))
        print("Złożona, styczne, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "4", -2, 2, lista[0], lista_zlozona)

        lista = (mb.metoda_bisekcji("4", "0", 10, 0-2, 2, lista_zlozona))
        print("Złożona, bisekcja, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "4", -2, 2, lista[0], lista_zlozona)

        lista = (ms.metoda_stycznych("4", "0", 10, -2, 2))
        print("Złożona, styczne, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "4", -2, 2, lista[0], lista_zlozona)

        #  - - znak pochodnej rozny na przedziale - -
    def test_something_else(self):
        lista_wielomian = [-3, 5, 2]
        lista = (mb.metoda_bisekcji("1", "A", 0.01, -2, 2, lista_wielomian))
        print("Wielomian, bisekcja, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", -2, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "A", 0.01, -2, 2))
        print("Wielomian, styczne, A", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", -2, 2, lista[0], lista_wielomian)

        lista = (mb.metoda_bisekcji("1", "B", 0.01, -2, 2, lista_wielomian))
        print("Wielomian, bisekcja, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", -2, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "B", 0.01, -2, 2))
        print("Wielomian, styczne, B", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", -2, 2, lista[0], lista_wielomian)

        lista = (mb.metoda_bisekcji("1", "0", 10, -2, 2, lista_wielomian))
        print("Wielomian, bisekcja, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("1", "1", -2, 2, lista[0], lista_wielomian)

        lista = (ms.metoda_stycznych("1", "0", 10, -2, 2))
        print("Wielomian, styczne, iteracje", "{:.6f}".format(lista[0]), lista[1])
        # f.rysuj_wykres("2", "1", -2, 2, lista[0], lista_wielomian)
