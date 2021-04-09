from rezept import Rezept
# logik
name = input('name bitte')
art = input('vegan oder was')
zutaten = input('zutaten mit mengenangabe')
zubereitung = input('text bitte für zubereitung')

zutatenliste = zutaten.split(',')


neues_gericht = Rezept(name, art, zutatenliste, zubereitung)
user = Rezept('essen', 'deff', 'def', 'erfg')
neues_gericht.gericht_ausgeben()