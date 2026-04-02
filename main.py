import functions

def menu():
    functions.clearTerminal()
    print("CLI Todo-List")
    print("-------------")
    print("1) Show tasks.")
    print("2) Edit tasks")
    print("3) Close")



while(True):
    menu()
    response = input("")
    match(response):
        case "1":
            functions.showTasks()
        case "2":
            functions.editTasks()
        case "3":
            exit()
        case _:
            print("Invalid Option")
        