import client as c
import materiel as m
import technicien as t
from enum import Enum
from datetime import date

class TypeIntervention(Enum):
    entr = "Entretien"
    dep = "Dépannage"

class Intervention:
    def __init__(self, id, type_intervention, date_i, materiel, technicien):
        self.set_id(id)
        self.set_type(type_intervention)
        self.set_date(date_i)
        self.set_materiel(materiel)
        self.set_technicien(technicien)

    def __str__(self):
        return f"ID Entretien: {self.__id}, Type: {self.__type.value}, Date: {self.__date}, Materiel: {self.__materiel.get_marque()} {self.__materiel.get_modele()} ({self.__materiel.get_id_materiel()}), Technicien: {self.__technicien}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
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

    def set_date(self, date_i):
        if isinstance(date_i, date):
            self.__date = date_i
        else:
            raise TypeError("La date doit être composée de trois entiers (jour, mois, année).")

    def get_materiel(self):
        return self.__materiel

    def set_materiel(self, materiel):
        if isinstance(materiel, m.Materiel):
            self.__materiel = materiel
        else:
            raise TypeError("Le matériel doit être un objet de type Materiel.")

    def get_technicien(self):
        return self.__technicien

    def set_technicien(self, technicien):
        if isinstance(technicien, t.Technicien):
            self.__technicien = technicien
        else:
            raise TypeError("Le technicien doit être un objet de type Technicien.")

def register_intervention(clients, techniciens, interventions, zones, historique):
    print("\n===== ENREGISTREMENT D'UNE INTERVENTION =====")
    client = c.search_client(clients)
    if not client: return
    materiel = m.search_materiel(client)
    print("Sélectionnez le(s) technicien(s) affecté(s) -> ")
    techniciens_assignes = t.search_technicien(techniciens, zones)
    while True:
        dates_str = input("\nDate(s) de l'intervention (jj/mm/aaaa, séparées par des espaces) -> ").split()
        dates = []
        try:
            for x in dates_str:
                parts = x.split("/")
                if len(parts) == 3:
                    dates.append(date(int(parts[2]), int(parts[1]), int(parts[0])))
                else:
                    raise ValueError("-> Erreur : Format invalide.")
            if not dates:
                raise ValueError("-> Erreur : Aucune date saisie.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            choix_type = input("Type d'intervention (entr: Entretien, dep: Dépannage) -> ").strip().lower()
            type_intervention = TypeIntervention[choix_type]
            break
        except KeyError:
            print("-> Erreur : Type invalide.")
    count = 0
    for datev in dates:
        for technicien in techniciens_assignes:
            intervention = Intervention(max((i.get_id() for i in historique), default=0)+1, type_intervention, datev, materiel, technicien)
            if intervention.get_type() == TypeIntervention.entr:
                materiel.set_historique(intervention)
            if client.get_id() not in interventions.keys():
                interventions.update({client.get_id(): [intervention]})
            elif intervention not in interventions[client.get_id()]:
                interventions[client.get_id()].append(intervention)
            historique.append(intervention)
            count += 1 
            print(f"--> Intervention enregistrée : {intervention}")
    print(f"\n--> {count} intervention(s) enregistrée(s) pour le matériel {materiel} du client {client}")

def set_prix(prices, intervention=None):
    print("\n===== METTRE PRIX =====")
    if intervention is not None:
        while True:
            try:
                prix = int(input("Prix de ce type d'intervention -> "))
                prices.update({intervention.get_materiel().get_type_materiel(): {intervention.get_type(): prix}})
                break
            except ValueError as e:
                print(e)
    else:
        print("Choisir parmis les types de matériel:")
        for typeMateriel in m.TypeMateriel:
            print(f"{typeMateriel.full_name} ({typeMateriel.name})")
        while True:
            try:
                typeMateriel_str = input("Type de matériel ('fin' pour finir) -> ").strip().lower()
                if typeMateriel_str == "fin":
                    break
                typeMateriel = m.TypeMateriel[typeMateriel_str]
                typeIntervention = TypeIntervention[input("Type d'intervention (entr, dep) -> ")]
                prix = int(input("Prix de ce type d'intervention -> "))
                prices.update({typeMateriel: {typeIntervention: prix}})
            except ValueError as e:
                print(e)

def print_facture(interventions, clients, prices):
    try:
        if not interventions:
            raise ValueError("-> Erreur : Aucune intervention à facturer.")
    except ValueError as e:
        print(e)
        return
    print("\n===== IMPRESSION FACTURE =====")
    client = c.search_client(dict((c, clients[c]) for c in interventions.keys()))
    for intervention in interventions[client.get_id()]:
        if intervention.get_materiel().get_type_materiel() not in prices.keys() or intervention.get_type() not in prices[intervention.get_materiel().get_type_materiel()].keys():
            set_prix(prices, intervention)
    print("\n===== FACTURE =====")
    print(client)
    print("="*19)
    total = 0
    for intervention in interventions[client.get_id()]:
        print(f"> {intervention}")
        prix = prices[intervention.get_materiel().get_type_materiel()][intervention.get_type()]
        print(f"  Prix {intervention.get_type().value}: {prix}")
        total += prix
    print("="*19)
    print(f"Total: {total}")
    print("="*19)
    interventions.pop(client.get_id())