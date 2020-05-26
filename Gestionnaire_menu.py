import os


def Gestionnaire_menu():
    os.system('cls')

    Init = []
    Tableau_menu = [[] for i in range(3)]
    with open("Tableau_menu.txt", "r", encoding="utf8") as text_file:
        nb = int(text_file.readline(4))
        for i in range(1, nb + 1):
            Init.append(text_file.readline().rstrip('\n'))

        for k in Init:
            Tableau_menu[0].append(k[:20].rstrip(' '))
            Tableau_menu[1].append(k[20:40].rstrip(' '))
            Tableau_menu[2].append(int(k[40:]))

    print("--".center(92, "-"))
    print("{0:^32}".format("RESTO DU PEUPLE").center(92, "-"))
    print("{0:^32}".format("GESTIONS DU MENU").center(92, "-"))
    print("--".center(92, "-"), '\n')

    print("--".center(92, "-"))
    print("|   {:30}|   {:30}|   {:19}|".format(
        "PLATS", "CATEGORIE", "PRIX"))
    print("--".center(92, "-"))
    for i in range(len(Tableau_menu[0])):
        print("| {:32}| {:32}| {:<21}|".format(
            Tableau_menu[0][i], Tableau_menu[1][i],
            str(Tableau_menu[2][i]) + ' €'))
    print("--".center(92, "-"))

    print("\n{:60}{}".format(
        "1. MODIFIER UN PLAT", "2. AJOUTER UN PLAT"))
    print("{:60}{}".format(
        "3. SUPPRIMER UN PLAT", "4. RETOUR AU MENU PRINCIPAL"))

    choice = 0
    while choice != 4:
        choice = int(input(
            "\nQUE VOULEZ VOUS FAIRE ? (1-4)  :  "))
        if choice == 1:
            MaJ(Tableau_menu)
        elif choice == 2:
            Ajouter(Tableau_menu)
        elif choice == 3:
            Supprimer(Tableau_menu)


def MaJ(Tableau_menu):
    MaJ = input(
        "\nQUEL PLAT VOULEZ-VOUS METTRE A JOUR ? : ")

    for i in range(len(Tableau_menu[0])):
        if Tableau_menu[0][i] == MaJ:
            Tableau_menu[0][i] = input("NOUVEAU NOM : ")
            Tableau_menu[1][i] = input("NOUVELLE CATEGORIE : ")
            Tableau_menu[2][i] = int(input("NOUVEAU PRIX : "))
    Sauvegarde(Tableau_menu)
    Gestionnaire_menu()


def Ajouter(Tableau_menu):
    nv = input(
        "\nQUEL PLAT QUE SOUHAITEZ-VOUS AJOUTER ? : ")
    Tableau_menu[0].append(nv)
    nv = input(
        "\nQUELLE EST SA CATEGORIE ? : ")
    Tableau_menu[1].append(nv)
    nv = int(input(
        "\nQUEL EST SON PRIX ? : "))
    Tableau_menu[2].append(nv)
    Sauvegarde(Tableau_menu)
    Gestionnaire_menu()


def Supprimer(Tableau_menu):
    suppr = input(
        "\nQUEL EST LE PRODUIT QUE VOUS SOUHAITEZ SUPPRIMER ? : ")
    for i in range(len(Tableau_menu[0])):
        if Tableau_menu[0][i] == suppr:
            Tableau_menu[0][i].pop(i)
            Tableau_menu[1][i].pop(i)
            Tableau_menu[2][i].pop(i)
    Sauvegarde(Tableau_menu)
    Gestionnaire_menu()


def Sauvegarde(Tableau_menu):
    text_file = open("Tableau_menu.txt", "w")
    text_file.write(str(len(Tableau_menu[0])))
    for i in range(len(Tableau_menu[0])):
        text_file.write("\n")
        Save = "{:20}{:20}{:4}".format(
            Tableau_menu[0][i], Tableau_menu[1][i], str(Tableau_menu[2][i]))
        text_file.write(Save)
    text_file.write("\n")
    text_file.close()
