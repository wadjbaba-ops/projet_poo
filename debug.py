import client as c
import technicien as t
import zone as z
import intervention as i
import materiel as m
from datetime import date

zones = {1: z.Zone(1, "Dakar", "Dakar", "Dakar")}
clients = {1: c.Client(1, "BurEquip")}
clients[1].add_materiel(m.Materiel(1, "HP", "200", clients[1], zones[1]))
techniciens = {1: t.Technicien(1, "Wadj", "Baba", zones[1])}
interventions_nf = {1: i.Intervention(1, i.TypeIntervention.dep, date(2005, 11, 9), clients[1].get_materiels()[1], techniciens[1])}
prices = {}
print(clients[1].show_materiels())