import materiel as m
import zone as z
import technicien as t
from datetime import timedelta

class Client:
    def __init__(self, id, nom):
        self.set_id(id)
        self.set_nom(nom)
        self.__adresses = {}
        self.__materiels = {}

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
            return "\n".join(f"{adresse}" for adresse in self.__adresses.values())

    def add_adresse(self, adresse):
        if not isinstance(adresse, z.Zone):
            raise TypeError("L'adresse doit être un objet de type Zone.")
        elif adresse.get_id() in self.__adresses.keys():
            raise ValueError("L'adresse existe déjà dans la liste des adresses du client.")
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
        if not self.__materiels:
            return "Aucun matériel enregistré."
        else:
            return "\n".join([f"{self.__materiels[id_materiel]}\n" for id_materiel in self.__materiels.keys()])

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
    print("===== ENGISTREMENT CLIENT =====")
    while True:
        try:
            name = input("Nom du nouveau client")
            if name.strip() == "":
                raise ValueError("Le nom ne peut être vide")
            else:
                break
        except ValueError as e:
            print(e)
    client = Client(max((i for i in clients.keys()), default=0)+1, name)
    adresse = t.search_zone(zones)
    client.add_adresse(adresse)
    clients.update({client.get_id(): client})
    return client

def sell_materiel(clients, zones):
    while True:
        try:
            c = int(input("Nouveau client ou client existant (1 ou 2) : "))
            if c not in [1, 2]:
                raise ValueError("Choix invalide")
            else:
                break
        except ValueError as e:
            print(e)
    if c == 1:
        client = register_client(clients, zones)
    else:
        client = search_client(clients)
    client.show_adresses()
    while True:
        try:
            c = int(input("Nouvelle adresse ou adresse existante (1 ou 2) : "))
            if c not in [1, 2]:
                raise ValueError("Choix invalide")
            else:
                break
        except ValueError as e:
            print(e)
    if c == 1:
            adresse = t.search_zone((zone for zone in zones if zone not in client.get_adresses().values()))
            client.add_adresse(adresse)
    else:
        adresse = t.search_zone(client.get_adresses())
    print("Choisir parmis la liste des types de matériel")
    for type in m.TypeMateriel:
        print(f"{type.full_name} ({type})")
    while True:
        try:
            type = m.TypeMateriel[input("Type de matériel : ")]
            break
        except ValueError as e:
            print(e)
    if type.period == timedelta():
        m.set_periode(type)
    while True:
        try:
            marque = input("Marque : ")
            if marque.strip() == "":
                raise ValueError("La marque ne peut pas être vide")
            else:
                break
        except ValueError as e:
            print(e)
    while True:
        try:
            modele = input("Modele : ")
            if modele.strip() == "":
                raise ValueError("La marque ne peut pas être vide")
            else:
                break
        except ValueError as e:
            print(e)
    materiel = m.Materiel(max((i for c in clients.values() for i in c.get_materiels().keys()), default=0)+1, marque, modele, client, adresse)
    client.add_materiel(materiel)
    print(materiel)

def search_client(clients):
    print("Choisissez parmis la liste des clients (identifiant) :\n")
    for client in clients.keys():
        print(clients[client])
    while True:
        try:
            client_id = int(input("Identifiant du client : "))
            if client_id not in clients.keys():
                raise ValueError("Erreur : ce client n'existe pas.")
            else:
                return clients[client_id]
        except ValueError as e:
            print(e)