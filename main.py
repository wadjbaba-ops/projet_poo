import client as c
import technicien as t
import zone as z
import intervention as i
import materiel as m
from datetime import date

zones = {1: z.Zone(1, "Dakar", "Dakar", "Dakar")}
clients = {1: c.Client(1, "BurEquip")}
clients[1].add_materiel(m.Materiel(1, "HP", "200", clients[1], zones[1], m.TypeMateriel.imp))
techniciens = {1: t.Technicien(1, "Wadj", "Baba", zones[1])}
interventions_nf = {1: [i.Intervention(1, i.TypeIntervention.dep, date(2005, 11, 9), clients[1].get_materiels()[1], techniciens[1])]}
prices = {}

def menu():
    print("===== MENU =====")
    print("1. Vendre matériel")
    print("2. Enregisterer Intervention")
    print("3. Facturer client")
    print("4. Gerer techniciens")

def menu_technicien():
    print("===== GERER TECHNICIENS =====")
    print("1. Embaucher technicien")
    print("2. Rechercher technicien")
    print("3. Ajouter spécialité à technicien")
    print("4. Muter technicien")
    print("5. Supprimer technicien")

while True:
    menu()
    while True:
        try:
            choix = int(input("-> "))
            if choix not in [1,2,3,4]:
                raise ValueError("Choix invalide")
            else:
                break
        except ValueError as e:
            print(e)
    match choix:
        case 1:
            c.sell_materiel(clients, zones)
        case 2:
            i.register_intervention(clients, techniciens, interventions_nf, zones)
        case 3:
            i.print_facture(interventions_nf, clients, prices)
        case 4:
            menu_technicien()
            while True:
                try:
                    choix = int(input("-> "))
                    if choix not in [1,2,3,4]:
                        raise ValueError("Choix invalide")
                    else:
                        break
                except ValueError as e:
                    print(e)
            match choix:
                case 1:
                    t.hire_technicien(techniciens, zones)
                case 2:
                    client = c.search_client(clients)
                    materiel = m.search_materiel(client)
                    t.assign_technicien(techniciens, materiel)
                case 3:
                    technicien = t.search_technicien(technicien)
                    t.add_specialite(technicien)
                case 4:
                    t.trans_technicien(techniciens, zones)
                case 5:
                    t.fire_technicien(techniciens)