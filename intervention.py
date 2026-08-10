from client import Client
from materiel import Materiel, TypeMateriel
from technicien import Technicien
from enum import Enum
from datetime import date

class TypeIntervention(Enum):
    entr = "Entretien"
    dep = "Dépannage"

class Intervention:
    def __init__(self, id_entretien, type_intervention, date, materiel, technicien):
        self.set_id(id_entretien)
        self.set_type(type_intervention)
        self.set_date(date)
        self.set_materiel(materiel)
        self.set_technicien(technicien)

    def __str__(self):
        return f"ID Entretien: {self.__id}, Type: {self.__type}, Date: {self.__date}, Materiel: {self.__materiel.marque} {self.__materiel.modele} ({self.__materiel.id_materiel}), Technicien: {self.__technicien}"

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
            self.__date = date(annee, mois, jour)
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

# def lauch_intervention(clients, techniciens):
#     print("Choisissez parmis la liste des clients (identifiant) :\n")
#     for     client in clients:
#         print(f"{clients[client].get_id()}: {clients[client].get_nom()}\n")
#     client_id = int(input("Identifiant du client : "))
#     if client_id not in clients:
#         raise ValueError("Erreur : ce client n'existe pas.")
#     else:
#         client = clients[client_id]

#     print("\nChoisissez parmis la liste des matériels du client (identifiant) :\n")
#     client.show_materiels()
#     materiel_id = int(input("Identifiant du matériel : "))
#     if materiel_id not in client.get_materiels():
#         raise ValueError("Erreur : ce matériel n'existe pas pour ce client.")
#     else:
#         materiel = client.get_materiels()[materiel_id]

#     techniciens_disponibles = [technicien for technicien in techniciens.values() if technicien.get_zone() == materiel.zone] 
#     print("\nChoisissez parmis la liste des techniciens disponibles (identifiant) :\n")
#     for technicien in techniciens_disponibles:
#         print(technicien)
#     technicien_id = int(input("Identifiant du technicien : "))
#     if technicien_id not in [technicien.get_id() for technicien in techniciens_disponibles]:
#         raise ValueError("Erreur : ce technicien n'est pas disponible pour cette zone.")
#     else:
#         technicien = techniciens[technicien_id]

def register_intervention(clients, techniciens, interventions):
    print("\n===== ENREGISTREMENT D'UNE INTERVENTION =====\n")
    print("Choisissez parmis la liste des clients (identifiant) :\n")
    for     client in clients:
        print(f"{clients[client].get_id()}: {clients[client].get_nom()}\n")
    client_id = int(input("Identifiant du client : "))
    if client_id not in clients:
        raise ValueError("Erreur : ce client n'existe pas.")
    else:
        client = clients[client_id]
    print("\nChoisissez parmis la liste des matériels du client (identifiant) :\n")
    client.show_materiels()
    materiel_id = int(input("Identifiant du matériel : "))
    if materiel_id not in client.get_materiels():
        raise ValueError("Erreur : ce matériel n'existe pas pour ce client.")
    else:
        materiel = client.get_materiels()[materiel_id]

    print("\nChoisissez parmis la liste des techniciens (identifiant) :\n")
    for technicien in techniciens:
        print(techniciens[technicien])
    technicien_ids = [int(x) for x in input("Identifiant(s) du technicien(s) separes par des espaces : ").split(" ")]
    for technicien_id in technicien_ids:
        if technicien_id not in techniciens:
            raise ValueError(f"Le technicien d'identifiant {technicien_id} n'existe pas.")
            technicien_ids.remove(technicien_id)

    dates = [date(int(x.split("/")[2]), int(x.split("/")[1]), int(x.split("/")[0])) for x in input("Dates de l'intervention (jj/mm/aaaa) separes par des espaces : ").split(" ")]
    type_intervention = TypeIntervention[input("Type d'intervention (entr pour Entretien, dep pour Dépannage) : ")]
    count = 0
    for date in dates:
        for technicien_id in technicien_ids:
            intervention = Intervention(len(materiel.historique_entretien) + 1, type_intervention, date, materiel, techniciens[technicien_id])
            materiel.historique_entretien.append(intervention)
            if client_id not in interventions.keys():
                interventions.update({client_id: [intervention]})
            else:
                interventions[client_id].append(intervention)
            count += 1 
            print(f"\nIntervention enregistrée : {intervention}")
        print(f"\n{count} intervention(s) enregistrée(s) pour le matériel {materiel.id_materiel}")

def set_prix(prices):
    print("\n===== METTRE PRIX =====\n")
    print("Choisir parmis les types de matériel")
    for typeMateriel in TypeMateriel.__members__:
        print(typeMateriel)
    typeMateriel = TypeMateriel[input("Type de matériel : ")]
    typeIntervention = TypeIntervention[input("Type d'intervention (entr, dep) : ")]
    prix = int(input("Prix de ce type d'intervention : "))
    prices.update({typeMateriel: {typeIntervention: prix}})

def print_facture(interventions, clients, prices):
    if not interventions:
        raise ValueError("Aucune intervention à facturer.")
    else:
        print("\n===== IMPRESSION FACTURE =====\n")
        print("Pour quel client : ")
        for client_id in interventions.keys():
            print(clients[client_id])
        client = clients[int(input("id du client : "))]
        print("\n===== FACTURE =====\n")
        print(client)
        total = 0
        for intervention in interventions[client.get_id()]:
            print(intervention)
            if intervention.get_materiel().get_typeMateriel() in prices.keys():
                if intervention.get_type() in prices[intervention.get_materiel().get_typeMateriel()].keys():
                    total += prices[intervention.get_materiel().get_typeMateriel()][intervention.get_type()]
                else:
                    prix = int(intput("Ajouter prix pour ce type d'intervention : "))
                    total += prix
                    prices[intervention.get_materiel().get_typeMateriel()].update({intervention.get_type(): prix})
            else:
                prix = int(intput("Ajouter prix pour ce type d'intervention : "))
                total += prix
                prices.update({intervention.get_materiel().get_typeMateriel(): {{intervention.get_type(): prix}}})
            print(f"Prix {intervention.get_type().value}: {prices[intervention.get_materiel().get_typeMateriel()][intervention.get_type()]}")
        print(f"Total: {total}")