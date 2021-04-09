# programm logik
from rezept import Rezept
print('Wenn Sie ein neues Rezept anlegen wollen geben sie "anlegen" ein!\nWenn Sie einen Vorschlag für ein Gericht haben'
      ' wollen drücken Sie einfach auf Enter')
befehl = input()

if befehl == 'anlegen':
    name_rezept = input('Name des Gerichts ? ')
    ernaehrungsform = input('tippe vegetarisches, veganes oder normales ')
    zutaten = input('Beispieleingabe: Milch 100ml, Mehl 300g, ')
    zubereitung = input('Kopiere den Text für die Zubereitung in dieses Feld.\n')
    zutatenliste = zutaten.split(',')

    neues_gericht = Rezept(name_rezept, ernaehrungsform, zutatenliste, zubereitung)
    #neues_gericht.append zu file
    print(f'Das Rezept  wurde zu Ihrem digitalen Kochbuch hinzugefügt! :)')

else:
    print('Hier ein Rezeptvorschlag !! Viel Spaß beim kochen')

neues_gericht1 = neues_gericht.gericht_anlegen()
neues_gericht1.