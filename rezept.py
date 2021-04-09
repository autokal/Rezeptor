class Rezept:
    def __init__(self, name_rezept, ernaehrungsform, zutatenliste, zubereitung):
        self.name = name_rezept
        self.form = ernaehrungsform
        self.zutaten = zutatenliste
        self.zubereitung = zubereitung

    def gericht_ausgeben(self):
        print(f'Gericht {self.name} ist ein {self.form} gericht\n {self.zutaten}\n {self.zubereitung}')

    def gericht_anlegen(self, name, art, zutatenliste, zubereitung):
        name = input('name bitte')
        art = input('vegan oder was')
        zutaten = input('zutaten mit mengenangabe')
        zubereitung = input('text bitte für zubereitung')

        zutatenliste = zutaten.split(',')

        neues_gericht = Rezept(name, art, zutatenliste, zubereitung)