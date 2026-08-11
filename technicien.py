from string import templatelib
from zone import Zone
from materiel import Materiel, TypeMateriel
from enum import Enum

class Specialite(Enum):
    exp = "Experimenté"
    nov = "Novice"

class Technicien:
    def __init__(self, id = None, nom = None, prenom = None, zone = None):
        self.set_id(id)
        self.set_nom(nom)
        self.set_prenom(prenom)
        self.set_zone(zone)
        self.__specialites = {}

    def __str__(self):
        return f"{self.__nom} {self.__prenom} ({self.__id})"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if id is not None and isinstance(id, int):
            self.__id = id
        else:
            pass

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if nom is not None:
            if not isinstance(nom, str):
                raise TypeError("Le nom doit être une chaîne de caractères.")
            elif nom.strip() == "":
                raise ValueError("Le nom ne peut pas être vide.")
            elif not nom.isalpha():
                raise ValueError("Le nom ne peut contenir que des caractères alphabétiques.")
        else:
            pass

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        if prenom is not None:
            if not isinstance(prenom, str):
                raise TypeError("Le prénom doit être une chaîne de caractères.")
            elif prenom.strip() == "":
                raise ValueError("Le prénom ne peut pas être vide.")
            elif not prenom.isalpha():
                raise ValueError("Le prénom ne peut contenir que des caractères alphabétiques.")
        else:
            pass

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
        if zone is not None and isinstance(zone, Zone):
            self.__zone = zone
        else:
            pass

def search_zone(zones):
    print("\nChoisissez parmis la liste des zones (identifiant) :\n")
    for zone in zones:
        print(zone)
    while True:
        try:
            zone = int(input("Identifiant de la zone : "))
            if zone not in zones:
                raise ValueError("Erreur : cette zone n'existe pas.")
            else:
                return zones[zone]
        except ValueError as e:
            print(e)

def hire_technicien(techniciens, zones):
    print("\n===== RECRUTEMENT D'UN TECHNICIEN =====\n")
    technicien = Technicien()
    while True:
        try:
            technicien.set_nom(input("Nom : "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            technicien.set_prenom(input("Prènom : "))
            break
        except ValueError as e:
            print(e)
    technicien.set_zone(search_zone(zones))
    add_specialite(technicien)
    technicien.set_id(max(techniciens.keys()) + 1 if techniciens else 1)
    techniciens.update({technicien.get_id(): technicien})

def search_technicien(techniciens):
    print("Choisissez parmis la liste des techniciens (identifiant) :\n")
    for id in techniciens.keys():
        print(techniciens[id])
    while True:
        try:
            technicien_ids = [int(x) for x in input("Identifiant(s) du technicien(s) separes par des espaces : ").split(" ") if int(x) in techniciens.keys()]
            if len(technicien_ids) == 0:
                raise ValueError("Erreur : aucun technicien trouvé.")
            return [techniciens[id] for id in technicien_ids]
        except ValueError as e:
            print(e)    

def add_specialite(technicien):
    print("\nChoisissez parmis la liste des spécialités (identifiant) :\n")
    for typeMateriel in TypeMateriel:
        print(f"{typeMateriel.name} ({typeMateriel})\n")
    while True:
        try:
            typeMateriel_str = input("Type de matériel : ").lower().strip()
            if typeMateriel_str == "fin":
                break
            else:
                typeMateriel = TypeMateriel[typeMateriel_str]
                specialite = Specialite[input("Spécialité (exp pour expérimenté, nov pour novice) : ").lower().strip()]
                technicien.set_specialite(typeMateriel, specialite)
        except ValueError as e:
            print(e)         
    

def assign_technicien(techniciens, materiel):
    techniciens_disponibles = [technicien for technicien in techniciens.values() if technicien.get_zone() == materiel.get_zone() and materiel.get_type_materiel() in technicien.get_specialites() and technicien.get_specialites()[materiel.get_type_materiel()] == Specialite.exp]
    if not  techniciens_disponibles:
        techniciens_disponibles = [technicien for technicien in techniciens.values() if technicien.get_zone() == materiel.get_zone() and materiel.get_type_materiel() in technicien.get_specialites()]
    if not techniciens_disponibles:
        raise ValueError("Erreur : aucun technicien disponible pour ce type de matériel dans cette.")
    else:
        print("\nChoisissez parmis la liste des techniciens disponibles (identifiant) :\n")
        for technicien in techniciens_disponibles:
            print(f"{technicien} : {technicien.get_specialites()[materiel.get_type_materiel()]}")
        while True:
            try:
                technicien_id = int(input("Identifiant du technicien : "))
                if technicien_id not in [technicien.get_id() for technicien in techniciens_disponibles]:
                    raise ValueError("Erreur : ce technicien n'est pas disponible pour cette zone et ce type de matériel.")
                else:
                    return techniciens[technicien_id]
            except ValueError as e:
                print(e)