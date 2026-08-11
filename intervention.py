from client import Client
from materiel import Materiel, TypeMateriel
from technicien import Technicien, search_technicien
from enum import Enum
from datetime import date

class TypeIntervention(Enum):
    entr = "Entretien"
    dep = "Dépannage"

class Intervention:
    def __init__(self, id, type_intervention, date, materiel, technicien):
        self.set_id(id)
        self.set_type(type_intervention)
        self.set_date(date)
        self.set_materiel(materiel)
        self.set_technicien(technicien)

    def __str__(self):
        return f"ID Entretien: {self.__id}, Type: {self.__type}, Date: {self.__date}, Materiel: {self.__materiel.marque} {self.__materiel.modele} ({self.__materiel.id_materiel}), Technicien: {self.__technicien}"

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
            self.__date = date(date_i)
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

def search_materiel(client):
    print("\nChoisissez parmis la liste des matériels du client (identifiant) :\n")
    client.show_materiels()
    materiel_id = int(input("Identifiant du matériel : "))
    while True:
        try:
            if materiel_id not in client.get_materiels():
                raise ValueError("Erreur : ce matériel n'existe pas pour ce client.")
            else:
                return client.get_materiels()[materiel_id]
        except ValueError as e:
            print(e)

def register_intervention(clients, techniciens, interventions):
    print("\n===== ENREGISTREMENT D'UNE INTERVENTION =====\n")
    client = search_client(clients)
    materiel = search_materiel(client)
    technicien_ids = search_technicien(techniciens)
    while True:
        try:
            dates_str = input("Dates de l'intervention (jj/mm/aaaa) separes par des espaces : ").split(" ")
            dates = []
            for x in dates_str:
                if len(x.split("/")) == 3:
                    dates.append(date(int(x.split("/")[2]), int(x.split("/")[1]), int(x.split("/")[0])))
                else:
                    raise ValueError("Erreur : format de date invalide.")
            if not dates:
                raise ValueError("Erreur : aucune date saisie.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            type_intervention = TypeIntervention[input("Type d'intervention (entr pour Entretien, dep pour Dépannage) : ")]
            break
        except ValueError as e:
            print(e)
            
    count = 0
    for date in dates:
        for technicien_id in technicien_ids:
            intervention = Intervention(max(i for m in clients.get_materiels().values() for i in m.get_historique().keys())+1, type_intervention, date, materiel, techniciens[technicien_id])
            materiel.historique_entretien.append(intervention)
            if client.get_id() not in interventions.keys():
                interventions.update({client.get_id(): [intervention]})
            else:
                interventions[client.get_id()].append(intervention)
            count += 1 
            print(f"\nIntervention enregistrée : {intervention}")
    print(f"\n{count} intervention(s) enregistrée(s) pour le matériel {materiel.id_materiel}")

def set_prix(prices):
    print("\n===== METTRE PRIX =====\n")
    print("Choisir parmis les types de matériel")
    for typeMateriel in TypeMateriel.__members__:
        print(typeMateriel)
    while True:
        try:
            typeMateriel_str = input("Type de matériel : ").strip().lower()
            if typeMateriel_str == "fin":
                break
            typeMateriel = TypeMateriel[typeMateriel_str]
            typeIntervention = TypeIntervention[input("Type d'intervention (entr, dep) : ")]
            prix = int(input("Prix de ce type d'intervention : "))
            prices.update({typeMateriel: {typeIntervention: prix}})
        except ValueError as e:
            print(e)

def print_facture(interventions, clients, prices):
    if not interventions:
        raise ValueError("Aucune intervention à facturer.")
    else:
        print("\n===== IMPRESSION FACTURE =====\n")
        client = search_client(clients)
        print("\n===== FACTURE =====\n")
        print(client)
        total = 0
        for intervention in interventions[client.get_id()]:
            print(intervention)
            if intervention.get_materiel().get_typeMateriel() in prices.keys():
                if intervention.get_type() in prices[intervention.get_materiel().get_typeMateriel()].keys():
                    total += prices[intervention.get_materiel().get_typeMateriel()][intervention.get_type()]
                else:
                    while True:
                        try:
                            prix = int(input("Ajouter prix pour ce type d'intervention : "))
                            break
                        except ValueError as e:
                            print(e)
                    total += prix
                    prices[intervention.get_materiel().get_typeMateriel()].update({intervention.get_type(): prix})
            else:
                while True:
                    try:
                        prix = int(input("Ajouter prix pour ce type d'intervention : "))
                        break
                    except ValueError as e:
                        print(e)
                total += prix
                prices.update({intervention.get_materiel().get_typeMateriel(): {intervention.get_type(): prix}})
            print(f"Prix {intervention.get_type().value}: {prices[intervention.get_materiel().get_typeMateriel()][intervention.get_type()]}")
        print(f"Total: {total}")
        interventions.pop(client.get_id())