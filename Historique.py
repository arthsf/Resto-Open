import os
import datetime as dt


def Historique():
    os.system('cls')

    Init = []
    Tableau_historique = [[] for i in range(2)]
    with open("Tableau_historique.txt", "r", encoding="utf8") as text_file:
        nb = int(text_file.readline(4))
        for i in range(1, nb + 1):
            Init.append(text_file.readline().rstrip('\n'))

        for k in Init:
            Tableau_historique[0].append(k[:14].rstrip(' '))
            Tableau_historique[1].append(int(k[14:]))

    k = 0
    while Soustraction_jour(Tableau_historique[0][k]) > 7:
        k += 1
    Profit = 0
    Moyenne = 0
    for i in range(len(Tableau_historique[1])):
        if i >= k:
            Profit += Tableau_historique[1][i]
    Moyenne = Profit / len(Tableau_historique[1])

    print("--".center(92, "-"))
    print("{0:^32}".format("RESTO DU PEUPLE").center(92, "-"))
    print("{0:^32}".format("HISTORIQUE DES COMMANDES").center(92, "-"))
    print("--".center(92, "-"), '\n')

    print("NOMBRE TOTALE DE COMMANDES PASSEES : ", len(Tableau_historique[1]))
    print("\nCOMMANDES PASSEE CES 7 DERNIERS JOURS : ",
          len(Tableau_historique[1]) - k)
    print("\nMONTANT TOTAL DES COMMMANDES CES 7 DERNIERS JOURS : ", Profit, '€')
    print("\nMONTANT MOYEN D'UNE COMMANDE : ", Moyenne, "€")

    print("\n\n{:60}{}".format(
        "1. EXPORTER LE RESUME", "2. RETOUR AU MENU PRINCIPAL"))

    choice = 0
    while choice != 2:
        choice = int(input("\nQUE VOULEZ VOUS FAIRE ? (1-2)  :  "))
        if choice == 1:
            Exporter(Tableau_historique, Profit, Moyenne, k)


def Exporter(Tableau_historique, Profit, Moyenne, k):
    dir = os.path.dirname(os.path.realpath('__file__'))
    with open(dir + "\\Historique\\" + dt.datetime.now()
              .strftime("%d-%m-%Y") + ".txt",
              "w+", encoding="utf-8")as file:
        file.write("--".center(92, "-"))
        file.write("\n" + "HISTORIQUE DES COMMANDES".center(92))
        file.write("\n" + dt.datetime.now()
                   .strftime("%d-%m-%Y").center(92))

        file.write("\n\nNOMBRE TOTALE DE COMMANDES PASSEES : " +
                   str(len(Tableau_historique[1])))
        file.write("\nCOMMANDES PASSEE CES 7 DERNIERS JOURS : " +
                   str(len(Tableau_historique[1]) - k))
        file.write("\nMONTANT TOTAL DES COMMMANDES CES 7 DERNIERS JOURS : " +
                   str(Profit) + "€")
        file.write("\nMONTANT MOYEN D'UNE COMMANDE : " +
                   str(Moyenne) + "€")


def Soustraction_jour(d):
    d1 = dt.datetime.strptime(
        dt.datetime.today().strftime("%d-%m-%Y"), "%d-%m-%Y")
    d2 = dt.datetime.strptime(d, "%d-%m-%Y")
    return abs((d2 - d1).days)
