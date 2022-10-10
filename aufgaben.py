import random

# --- Aufgabe 1: Listen ---
# --- Task 1: Lists ---

# Erstellen Sie eine 3x3-Liste, in der alle Felder mit 0 befüllt sind
#
# Create a 3x3 list, in which all fields are filled with 0
def create_3x3_list():
    eintraege = 3
    reihe = 3
    result = [[0]*eintraege ]*reihe 
    print(result)
    return result

# Erstellen Sie eine 3x3-Liste, in der jede Zahl anders ist
#
# Create a 3x3 list where each number is different
def create_3x3_list_different():
    eintraege, reihe = (3, 3)

    # Simple Array Result 0-8
    #index = 0
    #result = [[[] for i in range(eintraege)] for j in range(reihe)] 
    #for i in range(reihe):
    #    for j in range(eintraege):
    #        result[i][j]  = index
    #        index += 1

    #print("simple array result: ", result)

    result = [[[] for i in range(eintraege)] for j in range(reihe)] 
    numset = set()
    for i in range(reihe):
        for j in range(eintraege):
            num = random.randint(65,122)
            while num in numset:
                num = random.randint(65,122)

            result[i][j] = num 
            numset.add(result[i][j]) 

    return result


# mylist ist eine 3x3-Liste, wie sie von create_3x3_list_different() erstellt wird. Entfernen Sie das mittlere Element.
#
# mylist is a 3x3 list, like the one created by create_3x3_list_different(). Remove the middle element.
def remove_middle_element(mylist):
    result = mylist[:0] + mylist[1:]  

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
    #result = {item: chr(int(item)) for item in mylist} # bei 1D-Arrays
    #result = {mylist[i][j]:  chr(int(mylist[i][j])) for i in range(3) for j in range(3)} # jedem Eintrag wird ein Buchstabe zugewiesen (bei gleichen Einträgen keine doppelten)

    keys = ["a","b","c"] 
    index = 0
    result = dict()
    for i in mylist:
        tmpKey = keys[index] 
        result.update({tmpKey: i})
        index += 1

    return result


# --- Aufgabe 3: Strings ---
#
# --- Task 3: Strings ---

# Geben Sie den num-ten Buchstaben aus von text aus.
#
# Return the num-th character from text.
def get_char(text, num):
    result = text[num] 
    return result

    

# Das num-te Wort aus dem Satz sentence ausgeben.
#
# Return the num-th word from the sentence sentence (that consists of words separated by spaces).
def get_word(sentence, num):
    result = sentence.split(' ')
    return result[num] 



# Alle Wörter aus dem Satz mit "--" getrennt anstatt mit " " getrennt zurückgeben.
#
# Return a new string in which the words from the sentence are separated with "--" instead of " "
def join_by_dashes(sentence):
    result = sentence.replace(" ", "--")
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
    result = [char for char in text] 
    return result

# Geben Sie ein Array zurück, das von den Buchstaben des Wortes jeden nur ein Mal enthält. Beispiel:
# text = "test", result = ["t", "e", "s"]. Tip: Denken Sie an den Operator "in"
#
# Return an array just like the one from text_to_array, but containing each unique letter only once,
# e.g. text = "test", result = ["t", "e", "s"]. Hint: Remember the operator "in"
def text_to_unique_array(text):
    #return list(set(text)) # Reihenfolge ist hier falsch beim test

    unique = []
    for char in text:
        if char not in unique:
            unique.append(char) 

    return unique

# Drehen Sie die Zeichen in text um. Beispiel:
# text = "Zeichenkette", result="etteknehcieZ"
#
# Invert the text, e.g. text = "Zeichenkette", result="etteknehcieZ"
def invert_text(text):
    result = text[::-1] 
    return result

# Bauen Sie aus dem String text ein Array aller Rotationen. Beispiel:
# text = "test", result = ["test", "ttes", "stte", "estt"]
#
# Return an array containing all rotations of the text, e.g.
# text = "test", result = ["test", "ttes", "stte", "estt"]
def make_rotations(text):
    result = []  
    for i in range(len(text)):
        currentString = text[i:] + text[:i]  
        result.append(currentString)
    return result
