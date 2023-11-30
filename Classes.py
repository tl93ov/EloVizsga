from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def get_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

    def get_tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

    def get_tipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
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
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        if datum < today:
            print("Érvénytelen dátum, csak jövőbeni foglalásokat fogadunk el.")
            return

        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                print("A szoba már foglalt ezen a napon.")
                return

        self.foglalasok.append(Foglalas(szoba, datum))
        print("Sikeres foglalás.")

    def lemondas(self, szoba, datum):
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
