import materiel as m
import zone as z
import technicien as t
from datetime import timedelta, datetime

class Client:
    def __init__(self, id, nom):
        self.set_id(id)
        self.set_nom(nom)
        self.__adresses = {}
        self.__materiels = {}

    def __str__(self):
        return f"{self.__nom} ({self.__id})"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("L'identifiant doit être un entier.")

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str):
            self.__nom = nom
        else:
            raise TypeError("Le nom doit être une chaîne de caractères.")

    def get_adresses(self):
        return dict(self.__adresses)

    def show_adresses(self):
        if not self.__adresses:
            return "Aucune adresse enregistrée."
        else:
            return "\n".join(f"> {adresse}" for adresse in self.__adresses.values())

    def add_adresse(self, adresse):
        if not isinstance(adresse, z.Zone):
            raise TypeError("L'adresse doit être un objet de type Zone.")
        else:
            self.__adresses.update({adresse.get_id(): adresse})

    def remove_adresse(self, adresse):
        if not isinstance(adresse, z.Zone):
            raise TypeError("L'adresse doit être un objet de type Zone.")
        elif adresse.get_id() not in self.__adresses.keys():
            raise ValueError("L'adresse n'existe pas dans la liste des adresses du client.")
        else:
            del self.__adresses[adresse.get_id()]

    def get_materiels(self):
        return dict(self.__materiels)

    def show_materiels(self):
        if not self.__materiels.values():
            return "Aucun matériel enregistré."
        else:
            return "\n".join(f"> {materiel}" for materiel in self.__materiels.values())

    def add_materiel(self, materiel):
        if not isinstance(materiel, m.Materiel):
            raise TypeError("Le matériel doit être un objet de type Materiel.")
        elif materiel.get_id_materiel() in self.__materiels.keys():
            raise ValueError("Le matériel existe déjà dans la liste du matériel du client.")
        else:
            self.__materiels.update({materiel.get_id_materiel(): materiel})

    def remove_materiel(self, materiel):
        if not isinstance(materiel, m.Materiel):
            raise TypeError("Le matériel doit être un objet de type Materiel.")
        elif materiel.get_id_materiel() not in self.__materiels.keys():
            raise ValueError("Le matériel n'existe pas dans la liste du matériel du client.")
        else:
            del self.__materiels[materiel.get_id_materiel()]


def register_client(clients, zones):
    print("\n===== ENREGISTREMENT D'UN NOUVEAU CLIENT =====")
    while True:
        name = input("Nom du client -> ").strip()
        if name == "":
            print("-> Erreur : Le nom ne peut être vide.")
        else:
            break
    client_id = max(clients.keys(), default=0) + 1
    client = Client(client_id, name)
    print("Veuillez définir l'adresse principale du client:")
    client.add_adresse(z.search_zone(zones))
    clients[client.get_id()] = client
    print(f"\n--> Client {client} enregistré avec succès.")
    return client

def sell_materiel(clients, zones):
    print("\n===== VENTE DE MATÉRIEL =====")
    while True:
        try:
            c = int(input("1. Nouveau client\n2. Client existant\n-> "))
            if c not in [1, 2]:
                raise ValueError("-> Erreur : Choix invalide.")
            break
        except ValueError as e:
            print(e)
    client = register_client(clients, zones) if c == 1 else search_client(clients)
    adresse = z.search_zone(client.get_adresses())
    print("Liste des types de matériel disponibles :")
    for tm in m.TypeMateriel:
        print(f"> {tm.full_name} ({tm.name})")
    while True:
        try:
            choix_type = input("Saisissez le code du type de matériel -> ").strip().lower()
            type_mat = m.TypeMateriel[choix_type]
            break
        except KeyError:
            print("-> Erreur : Code de matériel inconnu.")
    if type_mat.period.days == 0:
        m.set_periode(type_mat)
    marque = input("Marque du matériel -> ").strip()
    modele = input("Modèle du matériel -> ").strip()
    mat_id = max((i for c in clients.values() for i in c.get_materiels().keys()), default=0) + 1
    materiel = m.Materiel(mat_id, marque, modele, client, adresse, type_mat)
    client.add_materiel(materiel)
    print(f"\n--> {materiel} vendu et enregistré avec succès.")

def search_client(clients):
    if not clients:
        print("-> Aucun client enregistré.")
        return
    print("Choisir parmis la liste des clients:")
    for client in clients.values():
        print(f"> {client}")
    while True:
        try:
            client_id = int(input("Veuillez saisir l'identifiant du client -> "))
            if client_id not in clients.keys():
                raise ValueError("-> Erreur : Ce client n'existe pas.")
            return clients[client_id]
        except ValueError as e:
            print(e)