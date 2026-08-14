class Zone:
    def __init__(self, id, designation, ville, departement):
        self.set_id(id)
        self.set_designation(designation)
        self.set_ville(ville)
        self.set_departement(departement)
        
    def __str__(self):
        return f"{self.__designation} ({self.__id})"
    
    def set_id(self, id):
        self.__id = id 
        
    def set_designation(self, designation):
        self.__designation = designation
        
    def set_ville(self, ville):
        self.__ville = ville
        
    def set_departement(self, departement):
        self.__departement = departement
        
    def get_id(self):
        return self.__id
        
    def get_designation(self):
        return self.__designation
    
    def get_ville(self):
        return self.__ville
    
    def get_departement(self):
        return self.__departement
    

def search_zone(zones):
    if len(zones) == 1:
        print(f"\n-->{list(zones.values())[0]} trouvée.")
        return list(zones.values())[0]
    print("Choisissez parmis la liste des zones (identifiant):")
    for zone in zones.values():
        print(f"> {zone}")
    while True:
        try:
            zone = int(input("Identifiant de la zone -> "))
            if zone not in zones.keys():
                raise ValueError("-> Erreur : cette zone n'existe pas.")
            else:
                return zones[zone]
        except ValueError as e:
            print(e)