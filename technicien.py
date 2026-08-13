import zone as z
import materiel as m
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
                self.__nom = nom
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
            else:
                self.__prenom = prenom
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
        elif not isinstance(typeMateriel, m.TypeMateriel):
            raise TypeError("Le type de matériel doit être une chaîne de caractères.")
        else:
            self.__specialites.update({typeMateriel: specialite})

    def get_zone(self):
        return self.__zone

    def set_zone(self, zone):
        if zone is not None and isinstance(zone, z.Zone):
            self.__zone = zone
        else:
            pass

def hire_technicien(techniciens, zones):
    print("\n===== RECRUTEMENT D'UN TECHNICIEN =====")
    technicien = Technicien()
    while True:
        try:
            technicien.set_nom(input("Nom -> "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            technicien.set_prenom(input("Prènom -> "))
            break
        except ValueError as e:
            print(e)
    technicien.set_zone(z.search_zone(zones))
    add_specialite(technicien)
    technicien.set_id(max(techniciens.keys()) + 1 if techniciens else 1)
    techniciens.update({technicien.get_id(): technicien})
    return technicien

def search_technicien(techniciens, zones):
    if not techniciens:
        print("--> Aucun technicien enregistré.")
        return
    print("\n===== LISTE DES TECHNICIENS =====")
    for tech in techniciens.values():
        print(f"> {tech}")
    while True:
        try:
            saisie = input("Identifiant(s) (séparés par un espace) -> ")
            technicien_ids = [int(x) for x in saisie.split() if int(x) in techniciens]
            if not technicien_ids:
                raise ValueError("-> Erreur : Aucun technicien valide sélectionné.")
            return [techniciens[i] for i in technicien_ids]
        except ValueError as e:
            print(e)  

def add_specialite(technicien):
    print("\n===== AJOUT D'UNE SPÉCIALITÉ =====")
    print("Types de matériel :")
    for tm in m.TypeMateriel:
        print(f"- {tm.full_name} ({tm.name})")
    while True:
        typeMateriel_str = input("Type de matériel (ou 'fin' pour terminer) -> ").lower().strip()
        if typeMateriel_str == "fin":
            break
        specialite_str = input("Niveau (exp: Expérimenté, nov: Novice) -> ").lower().strip()
        if typeMateriel_str in m.TypeMateriel.__members__ and specialite_str in Specialite.__members__:
            tm = m.TypeMateriel[typeMateriel_str]
            spec = Specialite[specialite_str]
            technicien.set_specialite(tm, spec)
            print("--> Spécialité ajoutée.")
        else:
            print("-> Erreur : Type de matériel ou niveau invalide.")       
    
def assign_technicien(techniciens, materiel):
    techniciens_disponibles = [technicien for technicien in techniciens.values() if technicien.get_zone() == materiel.get_adresse() and materiel.get_type_materiel() in technicien.get_specialites().keys() and technicien.get_specialites()[materiel.get_type_materiel()] == Specialite.exp]
    if not  techniciens_disponibles:
        techniciens_disponibles = [technicien for technicien in techniciens.values() if technicien.get_zone() == materiel.get_adresse() and materiel.get_type_materiel() in technicien.get_specialites().keys()]
    if not techniciens_disponibles:
        print("-> Aucun technicien disponible pour ce type de matériel dans cette zone.")
    else:
        print("Choisissez parmis la liste des techniciens disponibles (identifiant):")
        for technicien in techniciens_disponibles:
            print(f"{technicien} : {technicien.get_specialites()[materiel.get_type_materiel()].value}")
        while True:
            try:
                technicien_id = int(input("Identifiant du technicien -> "))
                if technicien_id not in (technicien.get_id() for technicien in techniciens_disponibles):
                    raise ValueError("-> Erreur : ce technicien n'est pas disponible pour cette zone et ce type de matériel.")
                else:
                    return techniciens[technicien_id]
            except ValueError as e:
                print(e)

def fire_technicien(techniciens):
    print("\n===== SUPPRIMER TECHNICIEN =====")
    technicien_ids = [i.get_id() for i in search_technicien(techniciens)]
    for technicien_id in technicien_ids:
        techniciens.pop(technicien_id)

def trans_technicien(techniciens, zones):
    print("\n===== TRANFERER TECHNICIEN =====")
    technicien_ids = (i.get_id() for i in search_technicien(techniciens))
    for technicien_id in technicien_ids:
        techniciens[technicien_id].set_zone(z.search_zone(zones))