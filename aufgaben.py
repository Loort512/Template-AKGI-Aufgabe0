# --- Aufgabe 1: Listen ---
# --- Task 1: Lists ---

# Erstellen Sie eine 3x3-Liste, in der alle Felder mit 0 befüllt sind
#
# Create a 3x3 list, in which all fields are filled with 0
def create_3x3_list():
    result = None # Hier None durch die richtige expression ersetzen
    # Replace None in the above line by the correct expression
    return result


# Erstellen Sie eine 3x3-Liste, in der jede Zahl anders ist
#
# Create a 3x3 list where each number is different
def create_3x3_list_different():
    result = None # Hier None durch die richtige expression ersetzen
    # Replace None in the above line by the correct expression
    return result


# mylist ist eine 3x3-Liste, wie sie von create_3x3_list_different() erstellt wird. Entfernen Sie das mittlere Element.
#
# mylist is a 3x3 list, like the one created by create_3x3_list_different(). Remove the middle element.
def remove_middle_element(mylist):
    result = mylist
    # Hier Dinge tun
    # Do things here
    return result


# --- Aufgabe 2: Dictionaries ---
#
# --- Task 2: Dictionaries ---

# Erstellen Sie aus den Elementen der Liste mylist (ein 3x3-Array wie aus create_3x3_list_different) eine
# Dictionary, in der die einzelnen Elemente Schlüsseln zugewiesen sind,
# die jeweils die Buchstaben (z.B. "a", "z" etc.)
#
# From the list mylist (which is a 3x3 array like the one returned by create_3x3_list_different), create
# a dictionary. In this dictionary, each of the values from mylist should be assigned to a key that is a string
# (e.g. "a", "z" etc. - it does not matter which letters you choose)
def convert_to_dict(mylist):
    result = None
    # Hier Dinge tun
    # Do things here
    return result


# --- Aufgabe 3: Strings ---
#
# --- Task 3: Strings ---

# Geben Sie den num-ten Buchstaben aus von text aus.
#
# Return the num-th character from text.
def get_char(text, num):
    result = None
    return result


# Das num-te Wort aus dem Satz sentence ausgeben.
#
# Return the num-th word from the sentence sentence (that consists of words separated by spaces).
def get_word(sentence, num):
    result = None
    return result


# Alle Wörter aus dem Satz mit "--" getrennt anstatt mit " " getrennt zurückgeben.
#
# Return a new string in which the words from the sentence are separated with "--" instead of " "
def join_by_dashes(sentence):
    result = None
    return result


# --- Aufgabe 4: Alles zusammen ---
#
# --- Task 4: Combining it all  ---

# AUFGABEN/TASKS:
# Geben Sie ein Array zurück, das in jedem Element der Reihe nach einen Buchstaben des Textes enthält. Beispiel:
# text = "test", result = ["t", "e", "s", "t"]
#
# Return an array that contains all the letters from text, e.g. text="test", result=["t", "e", "s", "t"]
def text_to_array(text):
    result = None
    return result

# Geben Sie ein Array zurück, das von den Buchstaben des Wortes jeden nur ein Mal enthält. Beispiel:
# text = "test", result = ["t", "e", "s"]. Tip: Denken Sie an den Operator "in"
#
# Return an array just like the one from text_to_array, but containing each unique letter only once,
# e.g. text = "test", result = ["t", "e", "s"]. Hint: Remember the operator "in"
def text_to_unique_array(text):
    result = None
    return result

# Drehen Sie die Zeichen in text um. Beispiel:
# text = "Zeichenkette", result="etteknehcieZ"
#
# Invert the text, e.g. text = "Zeichenkette", result="etteknehcieZ"
def invert_text(text):
    result = None
    return result

# Bauen Sie aus dem String text ein Array aller Rotationen. Beispiel:
# text = "test", result = ["test", "ttes", "stte", "estt"]
#
# Return an array containing all rotations of the text, e.g.
# text = "test", result = ["test", "ttes", "stte", "estt"]
def make_rotations(text):
    result = None
    return result
