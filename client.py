from materiel import Materiel
from zone import Zone

class Client:
    def __init__(self, id, nom):
        self.__id = id
        self.__nom = nom
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
        if isinstance(self.__nom, str):
            return self.__nom
        else:
            raise TypeError("Le nom doit être une chaîne de caractères.")

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
            return "\n".join(self.__adresses[adresse] for adresse in self.__adresses)

    def add_adresse(self, adresse):
        if not isinstance(adresse, Zone):
            raise TypeError("L'adresse doit être un objet de type Zone.")
        elif adresse in self.__adresses:
            raise ValueError("L'adresse existe déjà dans la liste des adresses du client.")
        else:
            self.__adresses.update({adresse.__id: adresse})

    def remove_adresse(self, adresse):
        if not isinstance(adresse, Zone):
            raise TypeError("L'adresse doit être un objet de type Zone.")
        elif adresse not in self.__adresses:
            raise ValueError("L'adresse n'existe pas dans la liste des adresses du client.")
        else:
            del self.__adresses[adresse.__id]

    def get_materiels(self):
        return dict(self.__materiels)

    def show_materiels(self):
        if not self.__materiels:
            return "Aucun matériel enregistré."
        else:
            return "\n".join([f"{self.__materiels[materiel].marque} {self.__materiels[materiel].modele} ({self.__materiels[materiel].id_materiel})\n" for materiel in self.__materiels])

    def add_materiel(self, materiel):
        if not isinstance(materiel, Materiel):
            raise TypeError("Le matériel doit être un objet de type Materiel.")
        elif materiel in self.__materiels:
            raise ValueError("Le matériel existe déjà dans la liste du matériel du client.")
        else:
            self.__materiels.update({materiel.id_materiel: materiel})

    def remove_materiel(self, materiel):
        if not isinstance(materiel, Materiel):
            raise TypeError("Le matériel doit être un objet de type Materiel.")
        elif materiel not in self.__materiels:
            raise ValueError("Le matériel n'existe pas dans la liste du matériel du client.")
        else:
            del self.__materiels[materiel.id_materiel]    