import intervention as i
import client as c
import zone as z
from enum import Enum
from datetime import timedelta, date

class TypeMateriel(Enum):
    pc = ("photocopieuse", timedelta())
    imp = ("imprimante", timedelta())
    cell = ("telephone cellulaire", timedelta())
    tel = ("telecopieuse", timedelta())
    mo = ("micro-ordinateur", timedelta())

    def __init__(self, full_name, period):
        self.full_name = full_name
        self.period = period

class Materiel:
    def __init__(self, id_materiel, marque, modele, client, adresse, typeMateriel, datev=date.today()):
        if not isinstance(id_materiel, int):
            raise ValueError("L'identifiant du matériel est obligatoire et doit être un entier.")
        if not isinstance(marque, str) or marque.strip() == "":
            raise ValueError("La marque est obligatoire.")
        if not isinstance(modele, str) or modele.strip() == "":
            raise ValueError("Le modèle est obligatoire.")
        if not isinstance(client, c.Client):
            raise ValueError("Le client est obligatoire.")
        if not isinstance(adresse, z.Zone):
            raise ValueError("L'adresse (Zone) est obligatoire.")
        if not isinstance(typeMateriel, TypeMateriel):
            raise ValueError("Le type de matériel doit être un objet TypeMateriel.")
        if not isinstance(datev, date):
            raise("La date de vente doit être de type date")

        self.__id_materiel = id_materiel
        self.__marque = marque
        self.__modele = modele
        self.__client = client
        self.__adresse = adresse
        self.__type_materiel = typeMateriel
        self.__date = datev
        self.__historique = {}

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

    def get_type_materiel(self):
        return self.__type_materiel

    def get_historique(self):
        return dict(self.__historique)

    def set_marque(self, marque):
        if not isinstance(marque, str) or marque.strip() == "":
            raise ValueError("La marque ne peut pas être vide.")
        self.__marque = marque

    def set_modele(self, modele):
        if not isinstance(modele, str) or modele.strip() == "":
            raise ValueError("Le modèle ne peut pas être vide.")
        self.__modele = modele

    def set_client(self, client):
        if not isinstance(client, c.Client):
            raise ValueError("Le client ne peut pas être vide.")
        self.__client = client

    def set_adresse(self, adresse):
        if not isinstance(adresse, z.Zone):
            raise ValueError("L'adresse ne peut pas être vide.")
        self.__adresse = adresse

    def set_historique(self, entretien):
        if not isinstance(entretien, i.Intervention):
            return
        if entretien.get_type() == i.TypeIntervention.entr:
            self.__historique.update({entretien.get_id(): entretien})

    def get_historique(self):
        return dict(self.__historique)

    def show_historique(self):
        return "\n".join(f"{entretien}" for entretien in self.__historique.values())

    def __str__(self):
        return f"{self.__marque} {self.__modele} ({self.__id_materiel})"

    def afficher(self):
        print("\n===== DÉTAILS DU MATÉRIEL =====")
        print(f"Identifiant : {self.get_id_materiel()}")
        print(f"Marque      : {self.get_marque()}")
        print(f"Modèle      : {self.get_modele()}")
        print(f"Client      : {self.get_client()}")
        print(f"Adresse     : {self.get_adresse()}")

    def get_date_entretien(self):
        if self.__historique:
            return list(self.__historique.values())[-1].get_date() + self.__type_materiel.period
        else:
            return self.__date + self.__type_materiel.period

def set_periode(typeMateriel=None):
    print("\n===== DÉFINIR LA PÉRIODE D'ENTRETIEN =====")
    if typeMateriel is not None:
        while True:
                try:
                    jours = int(input(f"Nombre de jours pour l'entretien de {typeMateriel.full_name} -> "))
                    typeMateriel.period = timedelta(days=jours)
                    print(f"\n--> Période mise à jour avec succès: {typeMateriel.period.days} jours.")
                    break
                except ValueError:
                    print("-> Erreur : Veuillez saisir un nombre entier de jours.")
    else:
        print("Types de matériel:")
        for tm in TypeMateriel:
            print(f"> {tm.full_name} ({tm.name})")
        while True:
            try:
                choix = input("Veuillez saisir le code du type de matériel -> ").strip().lower()
                tm = TypeMateriel[choix]
                jours = int(input(f"Nombre de jours pour l'entretien de {tm.full_name} -> "))
                tm.period = timedelta(days=jours)
                print(f"\n--> Période mise à jour avec succès : {tm.period.days} jours.")
                break
            except KeyError:
                print("-> Erreur : Type de matériel invalide.")
            except ValueError:
                print("-> Erreur : Veuillez saisir un nombre entier de jours.")

def search_materiel(client):
    print("\n===== SÉLECTION DU MATÉRIEL =====")
    print(client.show_materiels())
    while True:
        try:
            materiel_id = int(input("\nIdentifiant du matériel -> "))
            if materiel_id not in client.get_materiels():
                raise ValueError("-> Erreur : Ce matériel n'appartient pas à ce client.")
            return client.get_materiels()[materiel_id]
        except ValueError as e:
            print(e)

def notif_entretien(clients):
    today = date.today()
    for client in clients.values():
        for materiel in client.get_materiels().values():
            if materiel.get_type_materiel().period != timedelta():
                if today == (materiel.get_date_entretien() - timedelta(days=1)):
                    print("\n")
                    print("="*50)
                    print(f"Entretien de {materiel} du client {client} due demain")
                    print("="*50)
                elif today == (materiel.get_date_entretien()):
                    print("\n")
                    print("="*50)
                    print(f"Entretien de {materiel} du client {client} due aujourd'hui")
                    print("="*50)
                elif today > (materiel.get_date_entretien()):
                    print("\n")
                    print("="*50)
                    print(f"Entretien de {materiel} du client {client} étais due {materiel.get_date_entretien()}")
                    print("="*50)