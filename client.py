from materiel import Materiel

class Client:
    def __init__(self, id, nom):
        self.__id = id
        self.__nom = nom
        self.__adresses = []
        self.__materiels = []

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
        return self.__adresses

    def show_adresses(self):
        if not self.__adresses:
            return "Aucune adresse enregistrée."
        else:
            return "\n".join(self.__adresses)

    def add_adresse(self, adresse):
        if not isinstance(adresse, str):
            raise TypeError("L'adresse doit être une chaîne de caractères.")
        elif adresse in self.__adresses:
            raise ValueError("L'adresse existe déjà dans la liste des adresses du client.")
        else:
            self.__adresses.append(adresse)

    def remove_adresse(self, adresse):
        if not isinstance(adresse, str):
            raise TypeError("L'adresse doit être une chaîne de caractères.")
        elif adresse not in self.__adresses:
            raise ValueError("L'adresse n'existe pas dans la liste des adresses du client.")
        else:
            self.__adresses.remove(adresse)

    def get_materiel(self):
        return self.__materiels

    def add_materiel(self, adresse):
        if not isinstance(adresse, Materiel):
            raise TypeError("L'adresse doit être un objet de type Materiel.")
        elif adresse in self.__adresses:
            raise ValueError("Le matériel déjà dans la liste du matériel du client.")
        else:
            self.__adresses.append(adresse)

    def remove_adresse(self, adresse):
        if not isinstance(adresse, Materiel):
            raise TypeError("L'adresse doit être un objet de type Materiel.")
        elif adresse not in self.__adresses:
            raise ValueError("Le matériel n'existe pas dans la liste du matériel du client.")
        else:
            self.__adresses.remove(adresse)
    