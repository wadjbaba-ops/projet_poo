from materiel import Materiel
from technicien import Technicien
from enum import StrEnum

class TypeIntervention(StrEnum):
    entr = "Entretien"
    dep = "Dépannage"

class Intervention:
    def __init__(self, id_entretien, type_entretien, date, materiel, technicien):
        self.__id = self.set_id(id_entretien)
        self.__type = self.set_type(type_entretien)
        self.__date = []
        self.__materiel = self.set_materiel(materiel)
        self.__technicien = self.set_technicien(technicien)

    def __str__(self):
        return f"ID Entretien: {self.__id}, Type: {self.__type}, Date: {self.__date}, Materiel: {self.__materiel.marque} {self.__materiel.modele}, Technicien: {self.__technicien}"

    def get_id(self):
        return self.__id

    def set_id(self, id_entretien):
        if isinstance(id_entretien, int):
            self.__id = id_entretien
        else:
            raise TypeError("L'identifiant de l'entretien doit être un entier.")
        
    def get_type(self):
        return self.__type

    def set_type(self, type_entretien):
        if isinstance(type_entretien, TypeIntervention):
            self.__type = type_entretien
        else:
            raise TypeError("Le type d'entretien doit être un membre de l'enum TypeEntretien.")

    def get_date(self):
        return self.__date

    def set_date(self, jour, mois, annee):
        if isinstance(jour, int) and isinstance(mois, int) and isinstance(annee, int):
            self.__date = (jour, mois, annee)
        else:
            raise TypeError("La date doit être composée de trois entiers (jour, mois, année).")

    def get_materiel(self):
        return self.__materiel

    def set_materiel(self, materiel):
        if isinstance(materiel, Materiel):
            self.__materiel = materiel
        else:
            raise TypeError("Le matériel doit être un objet de type Materiel.")

    def get_technicien(self):
        return self.__technicien

    def set_technicien(self, technicien):
        if isinstance(technicien, Technicien):
            self.__technicien = technicien
        else:
            raise TypeError("Le technicien doit être un objet de type Technicien.")