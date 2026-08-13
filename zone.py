# # BUREQUIP SA - GESTION DES ZONES DES TECHNICIENS
# # Liste des techniciens
# techniciens = [
#     {"nom": "Moussa", "zone": "Dakar"},
#     {"nom": "Fatou", "zone": "Thiès"},
#     {"nom": "Ibrahima", "zone": "Dakar"},
#     {"nom": "Awa", "zone": "Saint-Louis"},
#     {"nom": "Ousmane", "zone": "Kaolack"},
#     {"nom": "Mariama", "zone": "Thiès"},
# ]

# # AFFICHER LES TECHNICIENS D'UNE ZONE
# def afficher_techniciens_zone(zone):
#     print(f"\nTechniciens de la zone : {zone}")

#     trouve = False

#     for technicien in techniciens:
#         if technicien["zone"].lower() == zone.lower():
#             print("-", technicien["nom"])
#             trouve = True

#     if not trouve:
#         print("Aucun technicien dans cette zone.")

# # AFFECTER UN TECHNICIEN À UNE INTERVENTION

# def affecter_technicien(zone):
#     print(f"\nRecherche d'un technicien dans la zone : {zone}")

#     for technicien in techniciens:
#         if technicien["zone"].lower() == zone.lower():
#             print( f"Technicien affecté : {technicien['nom']}" )
#             return technicien["nom"]
#     print("Aucun technicien disponible dans cette zone.")
#     return None
# # AFFICHER TOUTES LES ZONES

# def afficher_zones():
#     zones = set()

#     for technicien in techniciens:
#         zones.add(technicien["zone"])

#     print("\nZones couvertes par BurEquip SA")

#     for zone in sorted(zones):
#         print("-", zone)

# # PROGRAMME PRINCIPAL
# while True:

#     print("\n======================================")
#     print("     BUREQUIP SA - GESTION DES ZONES")
#     print("======================================")

#     print("1. Afficher toutes les zones")
#     print("2. Afficher les techniciens d'une zone")
#     print("3. Affecter un technicien à une zone")
#     print("0. Quitter")

#     choix = input("\nVotre choix : ")

#     if choix == "1":

#         afficher_zones()

#     elif choix == "2":

#         zone = input("Entrez la zone : ")
#         afficher_techniciens_zone(zone)

#     elif choix == "3":

#         zone = input(
#             "Entrez la zone de l'intervention : "
#         )

#         affecter_technicien(zone)

#     elif choix == "0":

#         print("Programme terminé.")
#         break

#     else:

#         print("Choix invalide.")
class Zone:
    def __init__(self,id,designation, ville, departement ):
        self.set_id(id)
        self.set_designation(designation)
        self.set_ville(ville)
        self.set_departement(departement)
    def set_id(self,id):
        self.__id=id 
    def set_designation(self,designation):
        self.__designation=designation
    def set_ville(self,ville):
        self.__ville=ville
    def set_departement(self,departement):
        self.__departement=departement
    def get_id(self):
        return self.__id
    def __str__(self):
        return f"{self.__designation} ({self.__id})"