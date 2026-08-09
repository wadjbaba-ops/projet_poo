class Client:
    def __init__(self, nom, prenom, email, telephone):
        self.__nom = nom
        self.__adresses = []

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