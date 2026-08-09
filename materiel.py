from enum import Enum

class TypeMateriel(Enum):
    pc = ("photocopieuse", 0)
    imp = ("imprimante", 0)
    cell = ("telephone cellulaire", 0)
    tel = ("telecopieuse", 0)
    mo = ("micro-ordinateur", 0)

    def __init__(self, name, period):
        self.name = name
        self.period = period

## utiliser des geters qui contiennent des gestion d'execption pour la methode __init__
## implementer les visibilités des attributs et donc ajouter des getters
## vous pouver prendre le fichier technicien comme referance
## ajouter un attribut historique des entretiens
class Materiel:
    def __init__(self, id_materiel, type, marque, modele, client, adresse, zone, periode):
        self.id_materiel = id_materiel
        self.type = type ## type de materiel
        self.marque = marque
        self.modele = modele
        self.client = client
        self.adresse = adresse
        self.zone = zone
        self.periode_entretien = periode ## periode d'entretien

    def afficher(self):
        print("\n===== MATERIEL =====")
        print("Identifiant :", self.id_materiel)
        print("Marque      :", self.marque)
        print("Modèle      :", self.modele)
        print("Client      :", self.client)
        print("Adresse     :", self.adresse)
        print("Zone        :", self.zone)

    def modifier(self):
        print("\n===== MODIFICATION DU MATERIEL =====")

        marque = input("Nouvelle marque : ")
        modele = input("Nouveau modèle : ")
        client = input("Nouveau client : ")
        adresse = input("Nouvelle adresse : ")
        zone = input("Nouvelle zone : ")

        if marque != "":
            self.marque = marque

        if modele != "":
            self.modele = modele

        if client != "":
            self.client = client

        if adresse != "":
            self.adresse = adresse

        if zone != "":
            self.zone = zone


def ajouter_materiel(liste_materiels):
    print("\n===== AJOUT D'UN MATERIEL =====")

    id_materiel = input("Identifiant du matériel : ")

    # Vérification de l'identifiant
    for materiel in liste_materiels:
        if materiel.id_materiel == id_materiel:
            print("Erreur : cet identifiant existe déjà.")
            return

    marque = input("Marque : ")
    modele = input("Modèle : ")
    client = input("Client : ")
    adresse = input("Adresse : ")
    zone = input("Zone : ")

    materiel = Materiel(
        id_materiel,
        marque,
        modele,
        client,
        adresse,
        zone
    )

    liste_materiels.append(materiel)

    print("Matériel ajouté avec succès.")


def afficher_materiels(liste_materiels):
    if len(liste_materiels) == 0:
        print("\nAucun matériel enregistré.")
        return

    print("\n===== LISTE DES MATERIELS =====")

    for materiel in liste_materiels:
        materiel.afficher()


def rechercher_materiel(liste_materiels):
    id_materiel = input("\nIdentifiant du matériel à rechercher : ")

    for materiel in liste_materiels:
        if materiel.id_materiel == id_materiel:
            materiel.afficher()
            return materiel

    print("Matériel introuvable.")
    return None


def supprimer_materiel(liste_materiels):
    id_materiel = input("\nIdentifiant du matériel à supprimer : ")

    for materiel in liste_materiels:
        if materiel.id_materiel == id_materiel:
            liste_materiels.remove(materiel)
            print("Matériel supprimé avec succès.")
            return

    print("Matériel introuvable.")


def modifier_materiel(liste_materiels):
    materiel = rechercher_materiel(liste_materiels)

    if materiel is not None:
        materiel.modifier()
        print("Matériel modifié avec succès.")
