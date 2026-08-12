from enum import Enum
from datetime import timedelta

class TypeMateriel(Enum):
    pc = ("photocopieuse", timedelta())
    imp = ("imprimante", timedelta())
    cell = ("telephone cellulaire", timedelta())
    tel = ("telecopieuse", timedelta())
    mo = ("micro-ordinateur", timedelta())

    def __init__(self, name, period):
        self.name = name
        self.period = period

## utiliser des geters qui contiennent des gestion d'execption pour la methode __init__
## implementer les visibilités des attributs et donc ajouter des getters
## vous pouver prendre le fichier technicien comme referance
## ajouter un attribut historique des entretiens
## ajouter une methode pour afficher la prochaine date d'entretien
## fonction pour assigner les periodes d'entretien
# materiel.py

class Materiel:

    def __init__(self, id_materiel, marque, modele, client, adresse, zone):
        try:
            if not isinstance(id_materiel, str) or id_materiel.strip() == "":
                raise ValueError("L'identifiant du matériel est obligatoire.")

            if not isinstance(marque, str) or marque.strip() == "":
                raise ValueError("La marque est obligatoire.")

            if not isinstance(modele, str) or modele.strip() == "":
                raise ValueError("Le modèle est obligatoire.")

            if not isinstance(client, str) or client.strip() == "":
                raise ValueError("Le client est obligatoire.")

            if not isinstance(adresse, str) or adresse.strip() == "":
                raise ValueError("L'adresse est obligatoire.")

            if not isinstance(zone, str) or zone.strip() == "":
                raise ValueError("La zone est obligatoire.")

            self.__id_materiel = id_materiel
            self.__marque = marque
            self.__modele = modele
            self.__client = client
            self.__adresse = adresse
            self.__zone = zone

        except ValueError as e:
            raise ValueError("Erreur lors de la création du matériel : " + str(e))

    def get_id_materiel(self):
        return self.__id_materiel

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_client(self):
        return self.__client

    def get_adresse(self):
        return self.__adresse

    def get_zone(self):
        return self.__zone

    def set_marque(self, marque):
        if not isinstance(marque, str) or marque.strip() == "":
            raise ValueError("La marque ne peut pas être vide.")
        self.__marque = marque

    def set_modele(self, modele):
        if not isinstance(modele, str) or modele.strip() == "":
            raise ValueError("Le modèle ne peut pas être vide.")
        self.__modele = modele

    def set_client(self, client):
        if not isinstance(client, str) or client.strip() == "":
            raise ValueError("Le client ne peut pas être vide.")
        self.__client = client

    def set_adresse(self, adresse):
        if not isinstance(adresse, str) or adresse.strip() == "":
            raise ValueError("L'adresse ne peut pas être vide.")
        self.__adresse = adresse

    def set_zone(self, zone):
        if not isinstance(zone, str) or zone.strip() == "":
            raise ValueError("La zone ne peut pas être vide.")
        self.__zone = zone

    def afficher(self):
        print("\n===== MATERIEL =====")
        print("Identifiant :", self.get_id_materiel())
        print("Marque      :", self.get_marque())
        print("Modèle      :", self.get_modele())
        print("Client      :", self.get_client())
        print("Adresse     :", self.get_adresse())
        print("Zone        :", self.get_zone())

    def modifier(self):
        print("\n===== MODIFICATION DU MATERIEL =====")

        marque = input("Nouvelle marque : ")
        modele = input("Nouveau modèle : ")
        client = input("Nouveau client : ")
        adresse = input("Nouvelle adresse : ")
        zone = input("Nouvelle zone : ")

        try:
            if marque != "":
                self.set_marque(marque)

            if modele != "":
                self.set_modele(modele)

            if client != "":
                self.set_client(client)

            if adresse != "":
                self.set_adresse(adresse)

            if zone != "":
                self.set_zone(zone)

            print("Matériel modifié avec succès.")

        except ValueError as e:
            print("Erreur :", e)

def ajouter_materiel(liste_materiels):
    print("\n===== AJOUT D'UN MATERIEL =====")

    id_materiel = input("Identifiant du matériel : ")

    # Vérification de l'identifiant
    for materiel in liste_materiels:
        if materiel.get_id_materiel() == id_materiel:
            print("Erreur : cet identifiant existe déjà.")
            return

    marque = input("Marque : ")
    modele = input("Modèle : ")
    client = input("Client : ")
    adresse = input("Adresse : ")
    zone = input("Zone : ")

    try:
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

    except ValueError as e:
        print("Erreur :", e)


def afficher_materiels(liste_materiels):

    if len(liste_materiels) == 0:
        print("\nAucun matériel enregistré.")
        return

    print("\n===== LISTE DES MATERIELS =====")

    for materiel in liste_materiels:
        materiel.afficher()

def rechercher_materiel(liste_materiels):

    id_materiel = input(
        "\nIdentifiant du matériel à rechercher : "
    )

    for materiel in liste_materiels:

        if materiel.get_id_materiel() == id_materiel:
            materiel.afficher()
            return materiel

    print("Matériel introuvable.")
    return None

def supprimer_materiel(liste_materiels):

    id_materiel = input(
        "\nIdentifiant du matériel à supprimer : "
    )

    for materiel in liste_materiels:

        if materiel.get_id_materiel() == id_materiel:
            liste_materiels.remove(materiel)
            print("Matériel supprimé avec succès.")
            return

    print("Matériel introuvable.")

def modifier_materiel(liste_materiels):

    materiel = rechercher_materiel(liste_materiels)

    if materiel is not None:
        materiel.modifier()

def set_periode(typeMateriel):
    print("===== METTRE PÉRIODE D'ENTRETIEN =====")
    print("\nChoisissez parmis la liste des spécialités (identifiant) :\n")
    for typeMateriel in TypeMateriel:
        print(f"{typeMateriel.name} ({typeMateriel})\n")
    while True:
        try:
            typeMateriel = TypeMateriel[input("Type matériel : ")]
            typeMateriel.period = timedelta(int(input("Nombre de jours : ")))
            break
        except ValueError as e:
            print(e)
    print(f"{typeMateriel.name} : {typeMateriel.period}")

def search_materiel(client):
    print("\nChoisissez parmis la liste des matériels du client (identifiant) :\n")
    client.show_materiels()
    materiel_id = int(input("Identifiant du matériel : "))
    while True:
        try:
            if materiel_id not in client.get_materiels():
                raise ValueError("Erreur : ce matériel n'existe pas pour ce client.")
            else:
                return client.get_materiels()[materiel_id]
        except ValueError as e:
            print(e)