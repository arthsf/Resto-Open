import os
from Commande import Commande
from Stock import Stock
from Gestionnaire_menu import Gestionnaire_menu
from Historique import Historique


def Menu_principal():
    os.system('cls')
    print("--".center(92, "-"))
    print("{0:^32}".format("RESTO DU PEUPLE").center(92, "-"))
    print("{0:^32}".format("18 RUE DU CUL").center(92, "-"))
    print("{0:^32}".format("TOMBOUKTOU").center(92, "-"))
    print("--".center(92, "-"))

    print("\nMENU PRINCIPAL :\n")

    print("1. PRISE DE COMMANDE")
    print("2. GESTION DES STOCK")
    print("3. GESTION DU MENU")
    print("4. HISTORIQUE DES COMMANDES")
    print("5. QUITTER")

    choice = 0
    while choice != 5:
        choice = int(input(
            "\nQUE VOULEZ VOUS FAIRE ? (1-5)  :  "))

        if choice == 1:
            Commande()
            Menu_principal()
            return
        elif choice == 2:
            Stock()
            Menu_principal()
            return
        elif choice == 3:
            Gestionnaire_menu()
            Menu_principal()
            return
        elif choice == 4:
            Historique()
            Menu_principal()
            return


if __name__ == "__main__":
    Menu_principal()
