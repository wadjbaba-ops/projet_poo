import client as c
import technicien as t
import zone as z
import intervention as i
import materiel as m
from datetime import date, timedelta

zones = {
    1: z.Zone(1, "Zone Dakar Centre", "Dakar", "Dakar"),
    2: z.Zone(2, "Zone Pikine", "Pikine", "Pikine"),
    3: z.Zone(3, "Zone Rufisque", "Rufisque", "Rufisque"),
    4: z.Zone(4, "Zone Thiès Centre", "Thiès", "Thiès"),
    5: z.Zone(5, "Zone Mbour", "Mbour", "Mbour")
}
clients = {1: c.Client(1, "Polytech"),
           2: c.Client(2, "Ecobank")}
clients[1].add_materiel(m.Materiel(1, "hp", "LaserJet", clients[1], zones[3], m.TypeMateriel.pc))
clients[1].add_materiel(m.Materiel(2, "EPSON", "P700", clients[1], zones[3], m.TypeMateriel.imp))
clients[2].add_materiel(m.Materiel(3, "Brother", "MFC Pro", clients[2], zones[1], m.TypeMateriel.tel))
clients[1].add_adresse(zones[3])
clients[2].add_adresse(zones[1])
clients[2].add_adresse(zones[4])
techniciens = {
    1: t.Technicien(1, "Wadj", "Baba", zones[1]),
    2: t.Technicien(2, "Baldé", "Youssouf", zones[3]),
    3: t.Technicien(3, "Laye", "Sène", zones[2])
}
techniciens[1].set_specialite(m.TypeMateriel.tel, t.Specialite.exp)
techniciens[3].set_specialite(m.TypeMateriel.imp, t.Specialite.nov)
techniciens[1].set_specialite(m.TypeMateriel.pc, t.Specialite.exp)
interventions_nf = {}
prices = {}
historique = []

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Vendre du matériel")
    print("2. Enregistrer une intervention")
    print("3. Facturer un client")
    print("4. Gestion techniciens")
    print("5. Gestion générale")
    print("6. Quitter")

def menu_utilitaire():
    print("\n===== GESTION GÉNÉRALE =====")
    print("1. Ajuster périodes d'entretien")
    print("2. Ajuster prix des interventions")
    print("3. Afficher historique")
    print("4. Afficher date entretien")
    print("5. Retour au menu principal")

def menu_technicien():
    print("\n===== GESTION DES TECHNICIENS =====")
    print("1. Embaucher un technicien")
    print("2. Assigner un technicien à un matériel")
    print("3. Ajouter une spécialité à un technicien")
    print("4. Muter un technicien")
    print("5. Renvoyer un technicien")
    print("6. Retour au menu principal")

while True:
    menu_principal()
    try:
        m.notif_entretien(clients)
        choix = int(input("\n--> "))
    except ValueError:
        print("-> Erreur : Veuillez entrer un nombre valide.")
        continue

    match choix:
        case 1:
            c.sell_materiel(clients, zones)
        case 2:
            i.register_intervention(clients, techniciens, interventions_nf, zones, historique)
        case 3:
            i.print_facture(interventions_nf, clients, prices)
        case 4:
            while True:
                menu_technicien()
                try:
                    choix_tech = int(input("\n --> "))
                except ValueError:
                    print("-> Erreur : Veuillez entrer un nombre valide.")
                    continue
                    
                match choix_tech:
                    case 1:
                        t.hire_technicien(techniciens, zones)
                    case 2:
                        client = c.search_client(clients)
                        if client:
                            materiel = m.search_materiel(client)
                            t.assign_technicien(techniciens, materiel)
                    case 3:
                        techs = t.search_technicien(techniciens, zones)
                        if techs:
                            t.add_specialite(techs[0])
                    case 4:
                        t.trans_technicien(techniciens, zones)
                    case 5:
                        t.fire_technicien(techniciens)
                    case 6:
                        break
                    case _:
                        print("-> Erreur : Choix invalide.")
        case 5:
            while True:
                menu_utilitaire()
                try:
                    choix_util = int(input("\n --> "))
                except ValueError:
                    print("-> Erreur : Veuillez entrer un nombre valide.")
                    continue
                    
                match choix_util:
                    case 1:
                        m.set_periode()
                    case 2:
                        i.set_prix(prices)
                    case 3:
                        client = c.search_client(clients)
                        materiel = m.search_materiel(client)
                        if materiel.get_historique():
                            print(f"\n===== HISTORIQUE ENTRETIEN {materiel} =====")
                            print(materiel.show_historique())
                        else:
                            print("\n--> Aucun entretien enregistré")
                    case 4:
                        client = c.search_client(clients)
                        materiel = m.search_materiel(client)
                        print(f"\n--> Prochaine date entretien {materiel}: {materiel.get_date_entretien()}")
                    case 5:
                        break
                    case _:
                        print("-> Erreur : Choix invalide.")
        case 6:
            print("\n===== FERMETURE DU PROGRAMME =====")
            break
        case _:
            print("-> Erreur : Choix invalide.")