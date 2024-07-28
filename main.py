
names = ["Kryštof", "Peter", "Juan", "Larry"]
surnames = ["Vaňous", "Deker", "Pedro", "Kent"]
age = ["22", "48", "36", "65"]
email = ["vanous.krystof@seznam.cz", "nous.petr@gmail.com", "pedrito.jui@loca.mx", "kent.arry@outlook.com"]

# a = int(input("Vyberte pozici:> ")) - 1

# print(names[a] + " " + surnames[a] + " " + age[a] + " " + email[a])



def display():
    list_of_lists = [names, surnames, age, email]
    for a in zip(*list_of_lists):
        print(*a)


def add():
    names.append(input("Please put in your name:> "))
    surnames.append(input("Please put in your surname:> "))
    age.append(str(input("Please put in your age:> ")))
    email.append(input("Please put in your email:> "))
def remove():
    n = input("Please put in the name that you wish to remove:> ")
    s = input("Please put in the surname that you wish to remove:> ")
    a = str(input("Please put in the age that you wish to remove:> "))
    e = input("Please put in the email that you wish to remove:> ")
    if n in names:
        names.remove(n)
    else:
        print(display())
        print("You must put in exact name that is on the list:> ")
        remove()
    if s in surnames:
        surnames.remove(s)
    else:
        print(display())
        print("You must put in exact surname that is on the list:> ")
        remove()
    if a in age:
        age.remove(a)
    else:
        print(display())
        print("You must put in exact age that is on the list:> ")
        remove()
    if e in email:
        email.remove(e)
    else:
        print(display())
        print("You must put in exact email that is on the list:> ")
        remove()


if __name__ == '__main__':
    print("Welcome to the Contact-book program.")
    print("You can display age and email of your contacts")
    print("You can add contacts to the list")
    print("You can remove contacts from the list")
    print("You can exit the program by putting in exit")
    print("Please choose accordingly to your desired action: display or add or remove or exit")

    while True:
        choice = input("> ")
        if choice == "display":
            display()
        elif choice == "add":
            add()
        elif choice == "remove":
            remove()
        elif choice == "exit":
            break
        else:
            print("Error!! Please put in one of the options: display/add/remove/exit")