from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Szoba(ABC):
    def __init__(self, szobaszam, ar, szalloda_nev):
        self.szobaszam = szobaszam
        self.ar = ar
        self.szalloda_nev = szalloda_nev

    @abstractmethod
    def get_tipus(self):
        pass

    def get_szalloda_nev(self):
        return self.szalloda_nev


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, szalloda_nev):
        super().__init__(szobaszam, 10000, szalloda_nev)

    def get_tipus(self):
        return "Egyágyas szoba"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, szalloda_nev):
        super().__init__(szobaszam, 15000, szalloda_nev)

    def get_tipus(self):
        return "Kétágyas szoba"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        szoba.szalloda_nev = self.nev
        self.szobak.append(szoba)


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        today = datetime.today()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)  # nullázzuk az időkomponenseket
        if datum < today:
            print("Érvénytelen dátum, csak jövőbeni foglalásokat fogadunk el.")
            return

        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                print(f"A(z) {szoba.get_szalloda_nev()} szálloda szobája már foglalt ezen a napon.")
                return

        szoba_ar = szoba.ar

        self.foglalasok.append(Foglalas(szoba, datum))

        foglalas_ar = szoba_ar

        print(f"Sikeres foglalás a(z) {szoba.get_szalloda_nev()} szállodában. A szoba ára naponta: {foglalas_ar} Ft.")

    def lemondas(self, szoba, datum):
        datum = datum.replace(hour=0, minute=0, second=0, microsecond=0)
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Sikeres lemondás.")
                return

        print("Nincs ilyen foglalás.")

    def listazas(self):
        print("Foglalások:")
        for foglalas in self.foglalasok:
            print(f"{foglalas.szoba.get_tipus()} - Szoba {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

