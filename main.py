from Classes import *

def main():
    szalloda = Szalloda("Hotel Python")  # Itt hozd létre a szállodát
    szalloda.add_szoba(EgyagyasSzoba(101, szalloda.nev))
    szalloda.add_szoba(KetagyasSzoba(201, szalloda.nev))
    szalloda.add_szoba(KetagyasSzoba(202, szalloda.nev))

    foglalas_kezelo = FoglalasKezelo()

    foglalas_kezelo.foglalas(szalloda.szobak[0], datetime(2023, 12, 1))
    foglalas_kezelo.foglalas(szalloda.szobak[1], datetime(2023, 12, 2))
    foglalas_kezelo.foglalas(szalloda.szobak[2], datetime(2023, 12, 3))
    foglalas_kezelo.foglalas(szalloda.szobak[0], datetime(2023, 12, 4))
    foglalas_kezelo.foglalas(szalloda.szobak[1], datetime(2023, 12, 5))

    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Választás: ")

        if valasztas == "1":
            szoba_tipus = input("Adja meg a szoba típusát (1 - Egyágyas, 2 - Kétágyas): ")
            szoba_szam = int(input("Adja meg a szoba számát 1-99-ig: "))
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")

            if szoba_tipus == "1":
                szoba = EgyagyasSzoba(100 + szoba_szam, szalloda.nev)  # Példa: egyágyas szoba számok: 101, 102, stb.
            elif szoba_tipus == "2":
                szoba = KetagyasSzoba(200 + szoba_szam, szalloda.nev)  # Példa: kétágyas szoba számok: 201, 202, stb.
            else:
                print("Érvénytelen szoba típus.")
                continue
            foglalas_kezelo.foglalas(szoba, datetime.strptime(datum, "%Y-%m-%d"))


        elif valasztas == "2":
            szoba_szam = int(input("Adja meg a szoba számát: "))
            szoba = None

            for sz in szalloda.szobak:
                if sz.szobaszam == szoba_szam:
                    szoba = sz
                    break

            if szoba is not None:
                datum = input("Adja meg a lemondás dátumát (YYYY-MM-DD): ")
                foglalas_kezelo.lemondas(szoba, datetime.strptime(datum, "%Y-%m-%d"))
            else:
                print("Nincs ilyen szoba.")

        elif valasztas == "3":
            foglalas_kezelo.listazas()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()