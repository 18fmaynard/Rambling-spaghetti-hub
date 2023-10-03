notes=[]

def add():
    print(notes)
    section = int(input("Which section would you like to edit?\nEnter the number or type new to create a new section."))
    section_1 = section - 1
    note = input("What is your note")
    if 0 <= section_1 <= len(notes):
        notes[section_1].append(note)
    elif section == "new":
        notes.append
        note = input("What is your note")
        end = len(notes)
        notes[end].append(note)
    else:
        add()
    print(notes)
def menu():
    choice = int(input("Do you want to:\n1. Add note\n2. Remove note\n3.Show notes"))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        show()
    else:
        menu()
menu()