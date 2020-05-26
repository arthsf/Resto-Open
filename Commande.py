import os
import datetime as dt


def Commande():
    os.system('cls')

    Init = []
    tab = [[] for i in range(3)]
    with open("Tableau_menu.txt", "r", encoding="utf8") as text_file:
        nb = int(text_file.readline(4))
        for i in range(1, nb + 1):
            Init.append(text_file.readline().rstrip('\n'))

        for k in Init:
            tab[0].append(k[:20].rstrip(' '))
            tab[1].append(k[20:40].rstrip(' '))
            tab[2].append(int(k[40:]))

    print("--".center(92, "-"))
    print("{0:^32}".format("RESTO DU PEUPLE").center(92, "-"))
    print("{0:^32}".format("PRISE DE COMMANDES").center(92, "-"))
    print("--".center(92, "-"), '\n')

    client = input("NOM DU CLIENT : ")
    nv_commande = [[] for i in range(3)]

    entrees = [[] for i in range(2)]
    plats = [[] for i in range(2)]
    boissons = [[] for i in range(2)]

    for i in range(len(tab[1])):
        if tab[1][i] == 'ENTREE':
            entrees[0].append(tab[0][i])
            entrees[1].append(tab[1][i])
        elif tab[1][i] == 'PLAT':
            plats[0].append(tab[0][i])
            plats[1].append(tab[2][i])
        elif tab[1][i] == 'BOISSON':
            boissons[0].append(tab[0][i])
            boissons[1].append(tab[2][i])

    print("\nENTREES DISPONNIBLES :")
    for i in entrees[0]:
        print(" -", i)

    print("\nPLATS DISPLONNIBLES :")
    for i in plats[0]:
        print(" -", i)

    print("\nBOISSONS DISPONNIBLES :")
    for i in boissons[0]:
        print(" -", i)

    print("\n{:60}{}".format(
        "1. SELECTIONNER UN PRODUIT",
        "2. RESUME DE LA COMMANDE"))
    print("{:60}{}".format(
        "3. ENVOIE DE LA COMMANDE A LA CUISINE",
        "4. RETOUR AU MENU PRINCIPAL"))

    choice = 0
    while choice != 4:
        choice = int(input("\nQUE VOULEZ VOUS FAIRE ? (1-4)  :  "))
        if choice == 1:
            nv_commande = Ajouter(tab, nv_commande)
        elif choice == 2:
            Resume(client, nv_commande)
        elif choice == 3:
            Export(client, nv_commande)


def Ajouter(tab, nv_commande):
    add = input('\nTAPEZ LE NOM DU LE PRODUIT : ')
    deja = False
    for i in range(len(tab[0])):
        if tab[0][i] == add:
            for j in range(len(nv_commande[0])):
                if tab[0][i] == nv_commande[0][j]:
                    nv_commande[2][j] += 1
                    deja = True
                    break
            if deja is False:
                nv_commande[0].append(tab[0][i])
                nv_commande[1].append(tab[2][i])
                nv_commande[2].append(1)
            break
    return nv_commande


def Resume(client, tab):
    print("--".center(92, "-"))
    print("RESUME DE LA COMMANDE".center(92))
    print("CLIENT : {}\n".format(client).center(92))
    for i in range(len(tab[0])):
        print(tab[2][i], 'x ', tab[0][i])
    total = 0
    for i in range(len(tab[1])):
        total += tab[1][i] * tab[2][i]
    print("COUT TOTAL DE LA COMMANDE : ", total, "€")
    input("\nAPPUYEZ SUR N'IMPORTE QUELLE TOUCHE POUR QUITTER LE RESUME")


def Export(client, nv_commande):
    dir = os.path.dirname(os.path.realpath('__file__'))
    with open(dir + "\\Commandes\\" + client + dt.datetime.now()
              .strftime(" %d-%m-%Y %H-%M") + ".txt", "w+", encoding="utf-8")\
            as file:
        file.write("--".center(92, "-") + "\n")
        file.write("RESUME DE LA COMMANDE".center(92) + "\n")
        file.write("CLIENT : {}\n".format(client).center(92) + "\n")
        for i in range(len(nv_commande[0])):
            file.write(str(
                nv_commande[2][i]) + 'x ' + nv_commande[0][i] + "\n")
        total = 0
        for i in range(len(nv_commande[1])):
            total += nv_commande[1][i] * nv_commande[2][i]
        file.write(
            "COUT TOTAL DE LA COMMANDE : " + str(total) + "€")

    Init = []
    Tableau_historique = [[] for i in range(2)]
    with open("Tableau_historique.txt", "r", encoding="utf8") as text_file:
        nb = int(text_file.readline(4))
        for i in range(1, nb + 1):
            Init.append(text_file.readline().rstrip('\n'))

        for k in Init:
            Tableau_historique[0].append(k[:14].rstrip(' '))
            Tableau_historique[1].append(int(k[14:]))
    Tableau_historique[0].append(dt.datetime.now().strftime("%d-%m-%Y"))
    Tableau_historique[1].append(total)

    text_file = open("Tableau_historique.txt", "w")
    text_file.write(str(len(Tableau_historique[0])))
    for i in range(len(Tableau_historique[0])):
        text_file.write("\n")
        Save = "{:14}{:4}".format(
            Tableau_historique[0][i], str(Tableau_historique[1][i]))
        text_file.write(Save)
    text_file.write("\n")
    text_file.close()
