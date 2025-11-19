from index import *

print("Menu :")
print("0: Quitter")
print("1: Ajouter des élèves")
print("2: Modifier le nom d'un élève")
print("3: Ajouter les notes d'un élève")
print("4: Modifier les notes d'un élève")
print("5: Supprimer un élève")

commandKey = int(input("Quelle touche voulez-vous utiliser ? "))

match commandKey:
    case 0:
        exit()
    case 1:
        nbStudent = int(input("Combien d'eleves voulez-vous ajouter ? "))

        for _ in range(nbStudent):
            name = input("Entrez le nom et le prénom de l'élève : ")
            addStudent(name, None)
    case 2:
        studentId = int(input("Entrez l'identifiant de l'élève : "))
        newName = input("Entrez le nouveau nom de l'élève : ")

        try:
            editStudentName(studentId, newName)
        except ValueError as e:
            print(e)
    case 3:
        addNotes(None, None)
    case 4:
        editNotes(None, None)
    case 5:
        studentName = input("Entrez le nom de l'élève à supprimer : ")

        try:
            deleteStudent(studentName)

            print(f"L'élève {studentName} a bien été supprimé.")
        except ValueError as e:
            print(e)
    case _:
        print("Vous n'avez pas utilisé un chiffre entre 0 et 5")
