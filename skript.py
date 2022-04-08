# Empfehlung (auch zum Danebenlegen bei den Übungsaufgaben): Python Cheat Sheet
# https://www.dataquest.io/blog/python-cheat-sheet/

# === Umgang mit Variablen allgemein ===

# Python-Skripte werden einfach von oben nach unten ausgefuehrt, es ist keine explizite main notwendig (aber moeglich, sehen wir spaeter)
# Variablen kriegen keine Typendeklaration:
x = 5
x += 3
y = 2*x
print(y)

# Grundlegende Operatoren funktionieren wie erwartet:
# Modulo:
print(y%3)

# Ganzzahl-Division (floor):
print(y//3)

# Potenzierung:
print(y**4)

# Alle Operationen lassen sich mit Direktzuweisung kombinieren:
y %= 3
print(y)

# Vorsicht: strong typing -> Java-artige Verkettung geht nicht!
print("y="+y)

# Stattdessen muss man explizit konvertieren:
print("y="+str(y))

# Jede Variable in Python ist ein Objekt:
print(x.bit_length())

# Nützliche Funktion: dir() zeigt alle Methoden und Attribute eines Objektes an:
dir(x)

# Das ist z.B. nützlich, um zu schauen, wie man etwas mit einem Objekt tut,
# wovon man vermutet, dass das Objekt es kann.
# Beispiel: Ich will wissen, wie ich einen String zu uppercase konvertiere.
# Dieser Befehl:
dir("   test")

# gibt mir eine Liste von Methoden von String. upper() sieht verdächtig nach dem
# aus, was ich tun will, mal schauen:
print("   test".upper())

# Methoden mit __ sind "magic"-Methoden, nicht für direkte Verwendung gedacht

# Neben den klassischen integer, float, string haben wir Listen:
x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
print(x)

# Vorsicht: Durch die dynamische Typisierung geht das x=[1,2,3] oben: x ist jetzt kein integer mehr, sondern eine Liste!
# Adressierung von Listen wie gewohnt:
print(x[0])

# Man kann mit Listen viele lustige Dinge tun, z.B.:
# slicen
print(x[2:5])
print(x[5:])
print(x[:5])

# von hinten adressieren
print(x[-3])

# Verketten, verschachteln und Datentypen darin mischen
print(x + ["a", 2, ["b", "blub"]])

# Wiederholen
zerolist = 4*[0]
print(zerolist)

# Elemente entfernen
x.pop(3) # Das ist der Index
print(x)
x.remove(5) # Das ist der Wert des Elements (es wird das erste Vorkommen gelöscht)
print(x)

# Mit dem Operator "in" kann man überprüfen, ob ein Element in einem Array vorhanden ist:
mylist = [0, 5, 7]
if 7 in mylist:
    print("7 is in the list!")
else:
    print("7 is not in the list!")

# Performance-Hinweis: Listen sind als voralloziierte pointer-Arrays implementiert, die bei Erreichen
# der Kapazität wachsen (-> volle Kopie).
# pop last, get sind O(1), append ist amortisiert O(1), aber pop nach Index, remove sind O(n)!

# --- Aufgabe 1: Listen (siehe aufgaben.py) ---


# Als abgespeckte Version existieren noch Tupel:
tup = (1, 3, 4)
print(tup)

# Viel mehr als Zugriff geht damit nicht, tuples sind immutable (erlauben
# aber Optimierungen, sollten also wenn möglich statt Listen eingesetzt werden)

# Dann gibt es noch Dictionaries (aus Java bekannt z.B. als HashMap):
mydict = {"key": "value", "a": 5, "Zeugs": "sehr sinnvoll", 7: "sieben"}
print(mydict)
print(mydict["Zeugs"])
mydict["Zeugs"] = "weniger sinnvoll"
print(mydict["Zeugs"])

# Ueberpruefung, ob ein key drin ist:
print("Zeugs" in mydict)
print("neuerkey" in mydict)
mydict["neuerkey"] = "neuerwert"
print("neuerkey" in mydict)
print(mydict["neuerkey"])

# Übrigens auch aus einem Tupel von Tupeln initialisierbar:
mydict2 = dict((("7", "sieben"), ("acht", 8)))
print(mydict2)

# --- Aufgabe 2: Dictionaries (siehe aufgaben.py) ---

# Ein set ist eine Menge und kann jedes Element nur ein Mal enthalten:

myset = set()
myset.add(15)
myset.add("blub")
print(myset)
myset.add(14)
myset.add(15)
print(myset)

# === Umgang mit Strings ===
# Python wird häufig zur Stringverarbeitung (Tabellenkonversion etc.) verwendet,
# daher ein paar mehr Details zu Strings.

# String-delimiter können ", ', oder (für multiline) """ sein:
print('Das ist z.B. nuetzlich um " nicht escapen zu muessen')

dat="""Oder um
mehrere Zeilen Text
einfach einzugeben"""
print(dat)

# Es existieren viele convenience-Funktionen für strings, z.B.:

dat2 = dat.replace("\n", " ")
print(dat2)
print(dat2.split(" "))

# (das geht alles auch mit regexp, Modul re, aber das führt zu weit)

# Strings haben eine häufig verwendete, nette Methode, um Tupel und Arrays zu verketten:

toprint = ["Das", "sind", "Woerter"]
print(" ".join(toprint))
print("--!--".join(toprint))

# --- Aufgabe 3: Strings ---

# Zum Formatieren von strings existiert eine Spezifikationssprache:
# {} sind placeholder für Variablen
x = 12
y = 4
print("Der Wert von y: {} minus den Wert von x: {} ist: {}".format(y, x, y-x))

# Mit {} können auch Positionen in der Argumentenliste angegeben werden:
print("y: {1}, x: {0}".format(x, y))

# Positionen können wiederholt werden:
print("{0}{1}{0}".format("abra", "cad"))

# Zahlenformate können definiert werden:
print("723 in binary: {0:b} and hex: {0:X}".format(723))

# Damit kann man übrigens schön die Ergebnisse binärer Operationen anschauen:
print("1: {:b}, 1<<2: {:b}, 60: {:b}, ~60: {:b} (dezimal: {}), 13: {:b}, 60&13: {:b}, 60|13: {:b} etc...".format(1, 1<<2, 60, ~60, ~60, 13, 60&13, 60|13))
# Frage: Kann jemand erklären, wieso ~60==-61

# Man kann links, rechts oder mittig alignen und sich das Fuellzeichen aussuchen:
print("y 10-stellig rechtsbündig: {0:>10}, linksbündig: {0:<10}, zentriert: {0:^10} und rechtsbündig mit 0: {0:0>10}".format(y))


# === Kontrollstrukturen ===

# Kontrollstrukturen verhalten sich wie gewohnt.
# Ungewohnt:
#  * Beginn eines Blocks wird mit : am Ende der Kontrollstuktur gekennzeichnet
#  * Einrückung muss stimmen (und in gesamten Code konsistent sein, mal 3 Leerzeichen und mal 4 geht nicht).
y = 12
if y > 10:
    y -= 3
elif y <= 10:
    y += 10
else:
    print("Das kann nicht passieren.")
print(y)

# Würde nicht funktionieren, wegen fehlender Einrückung:
#if y > 10:
#print("y immer noch groesser 10")

# While tut das, was while halt so tut:
y=10
while y > 5:
    print(y)
    y -= 1

# for ist zum iterieren da:
letters = ["a", "b", "c"]
for letter in letters:
    if letter == "a":
        print("AAAAAAAAA")
    print(letter)

# Man kann über alles iterieren, was iterable ist (auch strings sind z.B. iterable):
print(range(2,7))
for x in range(2,7):
    print(x)

for x in range(0,10,3):
    print(x)

for key in mydict:
    print(str(key) + ": " + str(mydict[key]))

for item in mydict.items():
    print(item)

# --- Aufgabe 4: Alles zusammen ---
