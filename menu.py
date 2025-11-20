from index import *

# Exemple de db pour les tests
# Base de donée
db = [
    {"name": "A", "notes": {"FR": [2, 4], "EN": [3, 5], "PE": [1, 6]}},
    {"name": "B", "notes": {"FR": [3, 4], "EN": [2, 5], "PE": [4, 6]}},
    {"name": "C", "notes": {"FR": [5, 4], "EN": [3, 1], "PE": [2, 6]}},
]


print("===== Menu utilisateur =====")
print("0: Quitter")
print("1: Ajouter des élèves")
print("2: Modifier le nom d'un élève")
print("3: Ajouter les notes d'un élève")
print("4: Modifier les notes d'un élève")
print("5: Supprimer un élève")

commandKey = int(input("Quelle touche voulez-vous utiliser ? "))


if commandKey == 0:
    exit()
elif commandKey == 1:
    nbStudent = int(input("Combien d'eleves voulez-vous ajouter ? "))

    for _ in range(nbStudent):
        name = input("Entrez le nom et le prénom de l'élève : ")
        addStudent(name, None, db)
elif commandKey == 2:
    studentId = int(input("Entrez l'identifiant de l'élève : "))
    newName = input("Entrez le nouveau nom de l'élève : ")

    try:
        editStudentName(studentId, newName , db)
    except ValueError as e:
        print(e)
elif commandKey == 3:
    fr = []
    en = []
    pe = []

    studentName =  input("Nom de l'élève ") 
    nbfr = int(input("Combien de notes voulez vous ajouté en francais"))
    for i in range(nbfr):
        frNotes = int(input("Qu'elle notes voulez vous ajouter en français :")) 
        fr.append(frNotes)
    nben = int(input("Combien de notes voulez vous ajouté en Anglais "))
    for i in range(nben):
        enNotes = int(input("Qu'elle notes voulez vous ajouter en anglais : "))
        en.append(enNotes)
    nbpe = int(input("Combien de notes voulez vous ajouté en sport"))
    for i in range(nbpe):
        peNotes = int(input("Qu'elle notes voulez vous ajouter en Sports :"))
        pe.append(peNotes)

    
    notes = {"FR": fr, "EN": en, "PE": pe}

    addNotes(studentName, notes , db)
    print(f"Vous avez ajouté {notes}; ")
    


elif commandKey == 4:
    fr = []
    en = []
    pe = []
    studentName =  input("Nom de l'élève ") 
    nbfr = int(input("Combien de notes voulez vous modifier en francais"))
    for i in range(nbfr):
        frNotes = int(input("Qu'elle notes voulez vous modifier en français :")) 
        fr.append(frNotes)
    nben = int(input("Combien de notes voulez vous modifier en Anglais "))
    for i in range(nben):
        enNotes = int(input("Qu'elle notes voulez vous modifier en anglais : "))
        en.append(enNotes)
    nbpe = int(input("Combien de notes voulez vous modifier en sport"))
    for i in range(nbpe):
        peNotes = int(input("Qu'elle notes voulez vous modifier en Sports :"))
        pe.append(peNotes)

    
    notes = {"FR": fr, "EN": en, "PE": pe}

    
    print(f"Vous avez ajouté {notes}; ") 
    editNotes(studentName, notes , db)
    
elif commandKey == 5:
    studentName = input("Entrez le nom de l'élève à supprimer : ")

    try:
        deleteStudent(studentName, db)

        print(f"L'élève {studentName} a bien été supprimé.")
    except ValueError as e:
        print(e)
else:
    print("Vous n'avez pas utilisé un chiffre entre 0 et 5")
