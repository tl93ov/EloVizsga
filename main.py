from Classes import *
def main():
    szalloda = Szalloda("Hotel Python")
    szalloda.add_szoba(EgyagyasSzoba(101))
    szalloda.add_szoba(KetagyasSzoba(201))
    szalloda.add_szoba(KetagyasSzoba(202))

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
            szoba_szam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            foglalas_kezelo.foglalas(szalloda.szobak[szoba_szam - 1], datetime.strptime(datum, "%Y-%m-%d"))

        elif valasztas == "2":
            szoba_szam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a lemondás dátumát (YYYY-MM-DD): ")
            foglalas_kezelo.lemondas(szalloda.szobak[szoba_szam - 1], datetime.strptime(datum, "%Y-%m-%d"))

        elif valasztas == "3":
            foglalas_kezelo.listazas()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
