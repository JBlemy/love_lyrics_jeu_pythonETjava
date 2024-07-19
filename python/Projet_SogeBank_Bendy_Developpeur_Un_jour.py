class Comptes:
    def __init__(self):
        self.numeroCpte = ''
        self.etat = 0
        self.solde = 0.0
        self.typeCompte = ''
        self.devise = ''

class Abonnes:
    def __init__(self):
        self.numCpte = ''
        self.nom = ''
        self.prenom = ''
        self.sexe = ''
        self.adresse = ''
        self.tel = ''

class Employes:
    def __init__(self):
        self.numEmp = ''
        self.nom = ''
        self.prenom = ''
        self.sexe = ''
        self.adresse = ''
        self.tel = ''
        self.salaire = 0.0

class Transactions:
    def __init__(self):
        self.numCompte = ''
        self.typeTransaction = ''
        self.nomAb = ''
        self.montant = 0.0

class Archives:
    def __init__(self):
        self.numEmp = ''
        self.numArch = ''
        self.nom = ''
        self.prenom = ''
        self.sexe = ''
        self.adresse = ''
        self.tel = ''
        self.salaire = 0.0

Cp = [Comptes() for i in range(10)]
ab = [Abonnes() for i in range(10)]
emp = [Employes() for i in range(10)]
tr = [Transactions() for i in range(10)]
arch = [Archives() for i in range(10)]

nbC = 0
nbA = 0
nbe = 0
nbt = 0
nbarch = 0

def testLongueurComptes(num):
    if len(num) != 10:
        return 1
    return 0

def testTypeComptes(type):
    if type != "Epargne" and type != "Courant":
        return 1
    return 0

def testChampVide(champ):
    if champ == "":
        return 1
    return 0

def testDevise(devise):
    if devise != "USD" and devise != "HTG":
        return 1
    return 0

def testDoublonCode(num):
    for i in range(nbC):
        if Cp[i].numeroCpte == num:
            return 1
    return 0

def testSexe(sexe):
    if sexe != "Féminin" and sexe != "Masculin":
        return 1
    return 0

def testTel(tel):
    if len(tel) != 12:
        return 1
    return 0

def menuGestionComptes():
    print("Menu Gestion Comptes")
    print("1. Enregistrer")
    print("2. Lister")
    print("3. Rechercher")
    print("4. Modifier")
    print("5. Supprimer")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuGestionEmployes():
    print("Menu Gestion Employés")
    print("1. Enregistrer")
    print("2. Lister")
    print("3. Rechercher")
    print("4. Modifier")
    print("5. Revoquer")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuGestionTransactions():
    print("Menu Gestion Transactions")
    print("1. Dépôt")
    print("2. Retrait")
    print("3. Transfert")
    print("4. Lister")
    print("5. Lister par type")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuGestionArchives():
    print("Menu Gestion Archives")
    print("1. Lister")
    print("2. Rechercher")
    print("3. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuPrincipal():
    print("Menu Principal")
    print("1. Gestion des comptes")
    print("2. Gestion des abonnés")
    print("3. Gestion des employés")
    print("4. Gestion des transactions")
    print("5. Gestion des archives")
    print("6. Quitter")
    ch = int(input("Faîtes votre choix: "))
    return ch

def enregistrerComptes():
    global nbC
    print("Enregistrement d'un compte")
    print("------------------------")
    numCpte = input("Numéro du compte: ")
    if testChampVide(numCpte) == 1:
        print("Le numéro du compte ne peut pas être vide.")
        return
    if testLongueurComptes(numCpte) == 1:
        print("Le numéro du compte doit avoir une longueur de 10 caractères.")
        return
    if testDoublonCode(numCpte) == 1:
        print("Le numéro du compte existe déjà.")
        return
    typeCompte = input("Type de compte (Epargne/Courant): ")
    if testChampVide(typeCompte) == 1:
        print("Le type de compte ne peut pas être vide.")
        return
    if testTypeComptes(typeCompte) == 1:
        print("Le type de compte doit être 'Epargne' ou 'Courant'.")
        return
    devise = input("Devise (USD/HTG): ")
    if testChampVide(devise) == 1:
        print("La devise ne peut pas être vide.")
        return
    if testDevise(devise) == 1:
        print("La devise doit être 'USD' ou 'HTG'.")
        return
    solde = input("Le solde : ")
    if testChampVide(solde) == 1:
        print("La devise ne peut pas être vide.")
        return
        
    Cp[nbC].numeroCpte = numCpte
    Cp[nbC].typeCompte = typeCompte
    Cp[nbC].devise = devise
    Cp[nbC].etat = 1
    Cp[nbC].solde = solde
    nbC += 1
    print("Le compte a été enregistré avec succès.")

def listerComptes():
    print("Liste des comptes")
    print("-----------------")
    for i in range(nbC):
        print("Numéro de compte:", Cp[i].numeroCpte)
        print("Type de compte:", Cp[i].typeCompte)
        print("Devise:", Cp[i].devise)
        print("État:", Cp[i].etat)
        print("Solde:", Cp[i].solde)
        print("-----------------")

def rechercherComptes():
    print("Recherche de compte")
    print("-------------------")
    numCpte = input("Numéro du compte: ")
    if testChampVide(numCpte) == 1:
        print("Le numéro du compte ne peut pas être vide.")
        return
    for i in range(nbC):
        if Cp[i].numeroCpte == numCpte:
            print("Numéro de compte:", Cp[i].numeroCpte)
            print("Type de compte:", Cp[i].typeCompte)
            print("Devise:", Cp[i].devise)
            print("État:", Cp[i].etat)
            print("Solde:", Cp[i].solde)
            print("-------------------")
            return
    print("Aucun compte trouvé avec ce numéro.")

def modifierComptes():
    print("Modification de compte")
    print("----------------------")
    numCpte = input("Numéro du compte: ")
    if testChampVide(numCpte) == 1:
        print("Le numéro du compte ne peut pas être vide.")
        return
    for i in range(nbC):
        if Cp[i].numeroCpte == numCpte:
            typeCompte = input("Nouveau type de compte (Epargne/Courant): ")
            if testChampVide(typeCompte) == 1:
                print("Le type de compte ne peut pas être vide.")
                return
            if testTypeComptes(typeCompte) == 1:
                print("Le type de compte doit être 'Epargne' ou 'Courant'.")
                return
            devise = input("Nouvelle devise (USD/HTG): ")
            if testChampVide(devise) == 1:
                print("La devise ne peut pas être vide.")
                return
            if testDevise(devise) == 1:
                print("La devise doit être 'USD' ou 'HTG'.")
                return
            Cp[i].typeCompte = typeCompte
            Cp[i].devise = devise
            print("Le compte a été modifié avec succès.")
            return
    print("Aucun compte trouvé avec ce numéro.")

def supprimerComptes():
    global nbC
    print("Suppression de compte")
    print("---------------------")
    numCpte = input("Numéro du compte: ")
    if testChampVide(numCpte) == 1:
        print("Le numéro du compte ne peut pas être vide.")
        return
    for i in range(nbC):
        if Cp[i].numeroCpte == numCpte:
            Cp[i].etat = 0
            Cp[i].solde = 0.0
            print("Le compte a été supprimé avec succès.")
            return
    print("Aucun compte trouvé avec ce numéro.")

def enregistrerEmployes():
    global nbe
    print("Enregistrement d'un employé")
    print("---------------------------")
    numEmp = input("Numéro de l'employé: ")
    if testChampVide(numEmp) == 1:
        print("Le numéro de l'employé ne peut pas être vide.")
        return
    nom = input("Nom de l'employé: ")
    if testChampVide(nom) == 1:
        print("Le nom de l'employé ne peut pas être vide.")
        return
    prenom = input("Prénom de l'employé: ")
    if testChampVide(prenom) == 1:
        print("Le prénom de l'employé ne peut pas être vide.")
        return
    sexe = input("Sexe de l'employé (Féminin/Masculin): ")
    if testChampVide(sexe) == 1:
        print("Le sexe de l'employé ne peut pas être vide.")
        return
    if testSexe(sexe) == 1:
        print("Le sexe de l'employé doit être 'Féminin' ou 'Masculin'.")
        return
    adresse = input("Adresse de l'employé: ")
    if testChampVide(adresse) == 1:
        print("L'adresse de l'employé ne peut pas être vide.")
        return
    tel = input("Téléphone de l'employé: ")
    if testChampVide(tel) == 1:
        print("Le téléphone de l'employé ne peut pas être vide.")
        return
    if testTel(tel) == 1:
        print("Le téléphone de l'employé doit avoir une longueur de 12 caractères.")
        return
    salaire = float(input("Salaire de l'employé: "))
    emp[nbe].numEmp = numEmp
    emp[nbe].nom = nom
    emp[nbe].prenom = prenom
    emp[nbe].sexe = sexe
    emp[nbe].adresse = adresse
    emp[nbe].tel = tel
    emp[nbe].salaire = salaire
    nbe += 1
    print("L'employé a été enregistré avec succès.")

def listerEmployes():
    print("Liste des employés")
    print("------------------")
    for i in range(nbe):
        print("Numéro de l'employé:", emp[i].numEmp)
        print("Nom de l'employé:", emp[i].nom)
        print("Prénom de l'employé:", emp[i].prenom)
        print("Sexe de l'employé:", emp[i].sexe)
        print("Adresse de l'employé:", emp[i].adresse)
        print("Téléphone de l'employé:", emp[i].tel)
        print("Salaire de l'employé:", emp[i].salaire)
        print("------------------")

def rechercherEmployes():
    print("Recherche d'employé")
    print("-------------------")
    numEmp = input("Numéro de l'employé: ")
    if testChampVide(numEmp) == 1:
        print("Le numéro de l'employé ne peut pas être vide.")
        return
    for i in range(nbe):
        if emp[i].numEmp == numEmp:
            print("Numéro de l'employé:", emp[i].numEmp)
            print("Nom de l'employé:", emp[i].nom)
            print("Prénom de l'employé:", emp[i].prenom)
            print("Sexe de l'employé:", emp[i].sexe)
            print("Adresse de l'employé:", emp[i].adresse)
            print("Téléphone de l'employé:", emp[i].tel)
            print("Salaire de l'employé:", emp[i].salaire)
            print("-------------------")
            return
    print("Aucun employé trouvé avec ce numéro.")

def modifierEmployes():
    print("Modification d'employé")
    print("----------------------")
    numEmp = input("Numéro de l'employé: ")
    if testChampVide(numEmp) == 1:
        print("Le numéro de l'employé ne peut pas être vide.")
        return
    for i in range(nbe):
        if emp[i].numEmp == numEmp:
            nom = input("Nouveau nom de l'employé: ")
            if testChampVide(nom) == 1:
                print("Le nom de l'employé ne peut pas être vide.")
                return
            prenom = input("Nouveau prénom de l'employé: ")
            if testChampVide(prenom) == 1:
                print("Le prénom de l'employé ne peut pas être vide.")
                return
            sexe = input("Nouveau sexe de l'employé (Féminin/Masculin): ")
            if testChampVide(sexe) == 1:
                print("Le sexe de l'employé ne peut pas être vide.")
                return
            if testSexe(sexe) == 1:
                print("Le sexe de l'employé doit être 'Féminin' ou 'Masculin'.")
                return
            adresse = input("Nouvelle adresse de l'employé: ")
            if testChampVide(adresse) == 1:
                print("L'adresse de l'employé ne peut pas être vide.")
                return
            tel = input("Nouveau téléphone de l'employé: ")
            if testChampVide(tel) == 1:
                print("Le téléphone de l'employé ne peut pas être vide.")
                return
            if testTel(tel) == 1:
                print("Le téléphone de l'employé doit avoir une longueur de 12 caractères.")
                return
            salaire = float(input("Nouveau salaire de l'employé: "))
            emp[i].nom = nom
            emp[i].prenom = prenom
            emp[i].sexe = sexe
            emp[i].adresse = adresse
            emp[i].tel = tel
            emp[i].salaire = salaire
            print("L'employé a été modifié avec succès.")
            return
    print("Aucun employé trouvé avec ce numéro.")

def revoquerEmployes():
    global nbe
    print("Révocation d'employé")
    print("--------------------")
    numEmp = input("Numéro de l'employé: ")
    if testChampVide(numEmp) == 1:
        print("Le numéro de l'employé ne peut pas être vide.")
        return
    for i in range(nbe):
        if emp[i].numEmp == numEmp:
            emp[i].nom = ""
            emp[i].prenom = ""
            emp[i].sexe = ""
            emp[i].adresse = ""
            emp[i].tel = ""
            emp[i].salaire = 0.0
            print("L'employé a été révoqué avec succès.")
            return
    print("Aucun employé trouvé avec ce numéro.")

def enregistrerTransactions():
    global nbt
    print("Enregistrement d'une transaction")
    print("-------------------------------")
    numCompte = input("Numéro de compte: ")
    if testChampVide(numCompte) == 1:
        print("Le numéro de compte ne peut pas être vide.")
        return
    typeTransaction = input("Type de transaction: ")
    if testChampVide(typeTransaction) == 1:
        print("Le type de transaction ne peut pas être vide.")
        return
    nomAb = input("Nom de l'abonné: ")
    if testChampVide(nomAb) == 1:
        print("Le nom de l'abonné ne peut pas être vide.")
        return
    montant = float(input("Montant de la transaction: "))
    tr[nbt].numCompte = numCompte
    tr[nbt].typeTransaction = typeTransaction
    tr[nbt].nomAb = nomAb
    tr[nbt].montant = montant
    nbt += 1
    print("La transaction a été enregistrée avec succès.")

def listerTransactions():
    print("Liste des transactions")
    print("----------------------")
    for i in range(nbt):
        print("Numéro de compte:", tr[i].numCompte)
        print("Type de transaction:", tr[i].typeTransaction)
        print("Nom de l'abonné:", tr[i].nomAb)
        print("Montant de la transaction:", tr[i].montant)
        print("----------------------")

def listerTransactionsType():
    print("Liste des transactions par type")
    print("------------------------------")
    typeTransaction = input("Type de transaction: ")
    if testChampVide(typeTransaction) == 1:
        print("Le type de transaction ne peut pas être vide.")
        return
    for i in range(nbt):
        if tr[i].typeTransaction == typeTransaction:
            print("Numéro de compte:", tr[i].numCompte)
            print("Type de transaction:", tr[i].typeTransaction)
            print("Nom de l'abonné:", tr[i].nomAb)
            print("Montant de la transaction:", tr[i].montant)
            print("------------------------------")
    print("Aucune transaction trouvée avec ce type.")

def listerArchives():
    print("Liste des archives")
    print("------------------")
    for i in range(nba):
        print("Numéro de compte:", arch[i].numCompte)
        print("Type de transaction:", arch[i].typeTransaction)
        print("Nom de l'abonné:", arch[i].nomAb)
        print("Montant de la transaction:", arch[i].montant)
        print("------------------")

def rechercherArchives():
    print("Recherche d'archive")
    print("-------------------")
    numCompte = input("Numéro de compte: ")
    if testChampVide(numCompte) == 1:
        print("Le numéro de compte ne peut pas être vide.")
        return
    for i in range(nba):
        if arch[i].numCompte == numCompte:
            print("Numéro de compte:", arch[i].numCompte)
            print("Type de transaction:", arch[i].typeTransaction)
            print("Nom de l'abonné:", arch[i].nomAb)
            print("Montant de la transaction:", arch[i].montant)
            print("-------------------")
            return
    print("Aucune archive trouvée avec ce numéro.")

def menuGestionComptes():
    print("Menu Gestion Comptes")
    print("1. Enregistrer un compte")
    print("2. Lister les comptes")
    print("3. Rechercher un compte")
    print("4. Modifier un compte")
    print("5. Supprimer un compte")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuGestionEmployes():
    print("Menu Gestion Employés")
    print("1. Enregistrer un employé")
    print("2. Lister les employés")
    print("3. Rechercher un employé")
    print("4. Modifier un employé")
    print("5. Révoquer un employé")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuGestionTransactions():
    print("Menu Gestion Transactions")
    print("1. Enregistrer une transaction")
    print("2. Lister les transactions")
    print("3. Lister les transactions par type")
    print("4. Lister les archives")
    print("5. Rechercher une archive")
    print("6. Retour au menu principal")
    ch = int(input("Faîtes votre choix: "))
    return ch

def menuPrincipal():
    print("Menu Principal")
    print("1. Gestion des comptes")
    print("2. Gestion des employés")
    print("3. Gestion des transactions")
    print("4. Quitter")
    ch = int(input("Faîtes votre choix: "))
    return ch

# Initialisation des variables
nbC = 0
nbe = 0
nbt = 0
nba = 0

# Structures de données
class Compte:
    def __init__(self):
        self.numeroCpte = ""
        self.typeCompte = ""
        self.devise = ""
        self.etat = 1
        self.solde = 0.0

class Employe:
    def __init__(self):
        self.numEmp = ""
        self.nom = ""
        self.prenom = ""
        self.sexe = ""
        self.adresse = ""
        self.tel = ""
        self.salaire = 0.0

class Transaction:
    def __init__(self):
        self.numCompte = ""
        self.typeTransaction = ""
        self.nomAb = ""
        self.montant = 0.0

class Archive:
    def __init__(self):
        self.numCompte = ""
        self.typeTransaction = ""
        self.nomAb = ""
        self.montant = 0.0

# Tableaux
Cp = [Compte() for i in range(100)]
emp = [Employe() for i in range(100)]
tr = [Transaction() for i in range(100)]
arch = [Archive() for i in range(100)]

# Boucle principale du programme
while True:
    choix = menuPrincipal()
    if choix == 1:
        while True:
            choix = menuGestionComptes()
            if choix == 1:
                enregistrerComptes()
            elif choix == 2:
                listerComptes()
            elif choix == 3:
                rechercherComptes()
            elif choix == 4:
                modifierComptes()
            elif choix == 5:
                supprimerComptes()
            elif choix == 6:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
    elif choix == 2:
        while True:
            choix = menuGestionEmployes()
            if choix == 1:
                enregistrerEmployes()
            elif choix == 2:
                listerEmployes()
            elif choix == 3:
                rechercherEmployes()
            elif choix == 4:
                modifierEmployes()
            elif choix == 5:
                revoquerEmployes()
            elif choix == 6:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
    elif choix == 3:
        while True:
            choix = menuGestionTransactions()
            if choix == 1:
                enregistrerTransactions()
            elif choix == 2:
                listerTransactions()
            elif choix == 3:
                listerTransactionsType()
            elif choix == 4:
                listerArchives()
            elif choix == 5:
                rechercherArchives()
            elif choix == 6:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
    elif choix == 4:
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
        