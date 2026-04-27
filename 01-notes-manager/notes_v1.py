# Notes Manager CLI

while True:
    print("---Notes Manager---")
    print("1. Add Notes")
    print("2. View Notes")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_text = input("Enter your note: ").strip()
        with open("notes.txt","a") as f:
            f.write(add_text + "\n")
            print("Note added! \n")
    elif choice == "2":
        with open("notes.txt","r") as f:
            print(f.read())
    elif choice == "3":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice! Try again.\n")
