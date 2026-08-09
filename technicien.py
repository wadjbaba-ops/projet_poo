from zone import Zone
from materiel import Materiel, TypeMateriel
from enum import StrEnum

class Specialite(StrEnum):
    exp = "Experimenté"
    nov = "Novice"

class Technicien:
    def __init__(self,id, nom, prenom, specialite, zone):
        self.__id = self.set_id(id)
        self.nom = nom
        self.prenom = prenom
        self.__specialites = {}
        self.__zone = self.set_zone(zone)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.__id})"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("L'identifiant doit être un entier.")

    def get_specialites(self):
        return self.__specialites

    def show_specialites(self):
        s = ""
        for typeMateriel, specialite in self.__specialites.items():
            s += f"{typeMateriel}: {specialite.value}\n"
        return s

    def set_specialite(self, typeMateriel, specialite):
        if not isinstance(specialite, Specialite):
            raise TypeError("La spécialité doit être un membre de l'enum Specialite.")
        elif not isinstance(typeMateriel, TypeMateriel):
            raise TypeError("Le type de matériel doit être une chaîne de caractères.")
        else:
            self.__specialites.update({typeMateriel: specialite})

    def get_zone(self):
        return self.__zone

    def set_zone(self, zone):
        if isinstance(zone, Zone):
            self.__zone = zone
        else:
            raise TypeError("La zone doit être un objet de type Zone.")