class Rezept:
    def __init__(self, name_rezept, ernaehrungsform, zutatenliste, zubereitung):
        self.name = name_rezept
        self.stil = ernaehrungsform
        self.zutaten = zutatenliste
        self.zubereitung = zubereitung

    #def send_meal_per_mail(self):
    def rezept_anzeigen(self):
        print(f'Hallo :) wie wäre es heute mit {self.name}, ein {self.stil} Gericht.\n\nbenötigte Zutaten:'
              f'\n{self.zutaten}\n\nZubereitung:\n {self.zubereitung}')




rezept1 = Rezept('kartoffel', 'vegetarisch', 'salz, kartoffel, wasser', 'Wasser kochen salz rein und essen')
rezept1.rezept_anzeigen()

