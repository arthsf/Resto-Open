import os
import datetime as dt


def Stock():
    os.system('cls')

    Init = []
    Tableau_Stock = [[] for i in range(2)]
    with open("Tableau_Stock.txt", "r", encoding="utf8") as text_file:
        nb = int(text_file.readline(4))
        for i in range(1, nb + 1):
            Init.append(text_file.readline().rstrip('\n'))

        for k in Init:
            Tableau_Stock[0].append(k[:20].rstrip(' '))
            Tableau_Stock[1].append(int(k[20:]))

    print("--".center(92, "-"))
    print("{0:^32}".format("RESTO DU PEUPLE").center(92, "-"))
    print("{0:^32}".format("GESTIONS DES STOCKS").center(92, "-"))
    print("--".center(92, "-"), '\n')

    print("--".center(92, "-"))
    print("|   {:66}|{:^20}|".format("PRODUITS", "QUANTITE"))
    print("--".center(92, "-"))
    for i in range(len(Tableau_Stock[0])):
        print("|{:69}| {:<19}|".format(
            Tableau_Stock[0][i], Tableau_Stock[1][i]))

    print("--".center(92, "-"))

    print("\n{:60}{}".format(
        "1. MISE A JOUR DU STOCK", "2. AJOUT DE PRODUITS"))
    print("{:60}{}".format(
        "3. EXPORTER LA LISTE DES PRODUITS", "4. SUPPRIMER UN PRODUIT"))
    print("5. RETOUR AU MENU PRINCIPAL")

    choice = 0
    while choice != 5:
        choice = int(input(
            "\nQUE VOULEZ VOUS FAIRE ? (1-5)  :  "))
        if choice == 1:
            MaJ(Tableau_Stock)
        elif choice == 2:
            Ajouter(Tableau_Stock)
        elif choice == 3:
            Exporter(Tableau_Stock)
        elif choice == 4:
            Supprimer(Tableau_Stock)


def MaJ(Tableau_Stock):
    MaJ = input(
        "\nDE QUEL PRODUIT VOULEZ-VOUS METTRE A JOUR LA QUANTITE ? : ")

    for i in range(len(Tableau_Stock[0])):
        if Tableau_Stock[0][i] == MaJ:
            Tableau_Stock[1][i] = int(input("NOUVELLE QUANTITE : "))
    Sauvegarde(Tableau_Stock)
    Stock()


def Ajouter(Tableau_Stock):
    nv = input(
        "\nQUEL EST LE PRODUIT QUE VOUS SOUHAITEZ AJOUTER ? : ")
    Tableau_Stock[0].append(nv)
    Tableau_Stock[1].append(0)
    Sauvegarde(Tableau_Stock)
    Stock()


def Exporter(Tableau_Stock):
    dir = os.path.dirname(os.path.realpath('__file__'))
    with open(dir + "\\Stocks\\" + dt.datetime.now()
              .strftime("%d-%m-%Y") + ".txt",
              "w+", encoding="utf-8")as file:
        file.write("--".center(92, "-"))
        file.write("|   {:66}|{:^20}|".format("PRODUITS", "QUANTITE"))
        file.write("--".center(92, "-"))
        for i in range(len(Tableau_Stock[0])):
            file.write("|{:69}| {:<19}|".format(
                Tableau_Stock[0][i], Tableau_Stock[1][i]))
        file.write("--".center(92, "-"))


def Supprimer(Tableau_Stock):
    suppr = input(
        "\nQUEL EST LE PRODUIT QUE VOUS SOUHAITEZ SUPPRIMER ? : ")
    for i in range(len(Tableau_Stock[0])):
        if Tableau_Stock[0][i] == suppr:
            Tableau_Stock[0][i].pop(i)
            Tableau_Stock[1][i].pop(i)
    Sauvegarde(Tableau_Stock)
    Stock()


def Sauvegarde(Tableau_Stock):
    text_file = open("Tableau_Stock.txt", "w")
    text_file.write(str(len(Tableau_Stock[0])))
    for i in range(len(Tableau_Stock[0])):
        text_file.write("\n")
        Save = "{:20}{:4}".format(
            Tableau_Stock[0][i], str(Tableau_Stock[1][i]))
        text_file.write(Save)
    text_file.write("\n")
    text_file.close()
