from zone import Zone
from materiel import Materiel, TypeMateriel
from enum import Enum

class Specialite(Enum):
    exp = "Experimenté"
    nov = "Novice"

class Technicien:
    def __init__(self,id, nom, prenom, zone):
        self.set_id(id)
        self.__nom = nom
        self.__prenom = prenom
        self.__specialites = {}
        self.set_zone(zone)

    def __str__(self):
        return f"{self.__nom} {self.__prenom} ({self.__id})"

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
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une chaîne de caractères.")
        elif nom.strip() == "":
            raise ValueError("Le nom ne peut pas être vide.")
        elif not nom.isalpha():
            raise ValueError("Le nom ne peut contenir que des caractères alphabétiques.")
        else:
            self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        if not isinstance(prenom, str):
            raise TypeError("Le prénom doit être une chaîne de caractères.")
        elif prenom.strip() == "":
            raise ValueError("Le prénom ne peut pas être vide.")
        elif not prenom.isalpha():
            raise ValueError("Le prénom ne peut contenir que des caractères alphabétiques.")
        else:
            self.__prenom = prenom

    def get_specialites(self):
        return dict(self.__specialites)

    def show_specialites(self):
        s = ""
        for typeMateriel in self.__specialites:
            s += f"{typeMateriel}: {self.__specialites[typeMateriel].value}\n"
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


def hire_technicien(techniciens, zones):
    print("\n===== RECRUTEMENT D'UN TECHNICIEN =====\n")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    print("\nChoisissez parmis la liste des zones (identifiant) :\n")
    for zone in zones:
        print(zone)
    zone = zones[int(input("Identifiant de la zone : "))]
    technicien = Technicien(len(techniciens) + 1, nom, prenom, zone)
    print("\nChoisissez parmis la liste des spécialités (identifiant) :\n")
    i = 0
    for typeMateriel in TypeMateriel:
        print(f"{typeMateriel.name} ({typeMateriel})\n")
    while True:
        typeMateriel_str = input("Type de matériel (ou 'fin' pour terminer) : ").lower()
        if typeMateriel_str == "fin":
            break
        else:
            specialite = Specialite[input("Spécialité (exp pour expérimenté, nov pour novice) : ").lower()]
            typeMateriel = TypeMateriel[typeMateriel_str]
            technicien.set_specialite(typeMateriel, specialite)
    techniciens.update({technicien.get_id(): technicien})

def add_specialite(techniciens):
    print("\n===== AJOUT D'UNE SPÉCIALITÉ À UN TECHNICIEN =====\n")
    print("Choisissez parmis la liste des techniciens (identifiant) :\n")
    for id in techniciens:
        print(techniciens[id])
    technicien_id = int(input("Identifiant du technicien : "))
    if technicien_id not in techniciens:
        raise ValueError("Erreur : ce technicien n'existe pas.")
    else:
        technicien = techniciens[technicien_id]
    print("\nChoisissez parmis la liste des spécialités (identifiant) :\n")
    for typeMateriel in TypeMateriel:
        print(f"{typeMateriel.name} ({typeMateriel})\n")
    typeMateriel = TypeMateriel[input("Type de matériel : ").lower()]
    specialite = Specialite[input("Spécialité (exp pour expérimenté, nov pour novice) : ").lower()]
    technicien.set_specialite(typeMateriel, specialite)
