db = [
    {"name": "A", "notes": {"FR": [2, 4], "EN": [3, 5], "PE": [1, 6]}},
    {"name": "B", "notes": {"FR": [3, 4], "EN": [2, 5], "PE": [4, 6]}},
    {"name": "C", "notes": {"FR": [5, 4], "EN": [3, 1], "PE": [2, 6]}},
]


# Add student with name and notes (if notes is None, create empty notes)
def addStudent(name: str, notes: dict):
    basicNotes = {"FR": [], "EN": [], "PE": []}

    db.append({"name": name, "notes": notes if notes else basicNotes})


# Edit student name by id (index in db)
def editStudentName(id: int, newName: str):
    for i in range(len(db)):
        if i == id:
            db[i]["name"] = newName
            break


# Delete student by name
def deleteStudent(name: str):
    for i in range(len(db)):
        if db[i]["name"] == name:
            del db[i]
            break
        else:
            raise ValueError("L'élève n'existe pas")


# Add notes to student by name
def addNotes(name: str, notes: dict):
    for i in range(len(db)):
        if db[i]["name"] == name:
            for subject in notes:
                db[i]["notes"][subject].extend(notes[subject])
            break


# Edit notes of student by name
def editNotes(name: str, notes: dict):
    for i in range(len(db)):
        if db[i]["name"] == name:
            for subject in notes:
                db[i]["notes"][subject] = notes[subject]
            break


# actions

# addStudent("D", None);
# editStudentName(1, "DD");
# deleteStudent("DD");
# addNotes("B", {'FR': [10,12],'EN': [14,15],'PE': [11,16]});
# editNotes("C", {'FR': [15,14],'EN': [13,11],'PE': [12,16]});
