# Ajouter un élève avec un nom et des notes (si les notes sont None, créer des notes vides)
def addStudent(name, notes, db):
    basicNotes = {"FR": [], "EN": [], "PE": []}

    db.append({"name": name, "notes": notes if notes else basicNotes})


# Changer le nom d'un élève par son identifiant
def editStudentName(id, newName, db):
    for i in range(len(db)):
        if i == id:
            db[i]["name"] = newName
            break
        else:
            raise ValueError("Nom personne inexistante dans le répertoire")


# Supprimer un élève par son nom
def deleteStudent(name, db):
    for i in range(len(db)):
        if db[i]["name"] == name:
            del db[i]
            break
        else:
            raise ValueError("Nom personne inexistante dans le répertoire")


# Ajouter des notes à un élève par son nom
def addNotes(name, notes, db):
    try:
        for i in range(len(db)):
            if db[i]["name"] == name:
                for subject in notes:
                    db[i]["notes"][subject].extend(notes[subject])
                break
    except ValueError:
        print("Nom personne inexistante dans le répertoire")


# Changer les notes d'un élève par son nom
def editNotes(name, notes, db):
    try:
        for i in range(len(db)):
            if db[i]["name"] == name:
                for subject in notes:
                    db[i]["notes"][subject] = notes[subject]
                break
    except ValueError:
        print("Nom personne inexistante dans le répertoire")


def number(arg):
    try:
        return int(arg)
    except ValueError:
        try:
            float(arg)
        except ValueError:
            print("This is not a number")

# actions

# addStudent("D", None);
# editStudentName(1, "DD");
# deleteStudent("DD");
# addNotes("B", {'FR': [10,12],'EN': [14,15],'PE': [11,16]});
# editNotes("C", {'FR': [15,14],'EN': [13,11],'PE': [12,16]});
