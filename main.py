import pandas

data = pandas.read_csv("contacts.csv", index_col="Name")
contact_dict = data.to_dict(orient="records")

accessing = True
print("\nWelcome to your contact book.")

while accessing:
    choice = input("\nIf you would like to see your contacts, enter 1."
          "\nIf you would like to create a contact, enter 2."
          "\nIf you would like to delete a contact, enter 3."
          "\nIf you would like to search your contacts, enter 4."
          "\nIf you would like to exit your contactbook, enter 5."
            "\nEnter here: ")
    if choice == "1":
        print(f"\n{data}")
    if choice == "2":
        with open("contacts.csv", "a") as file:
            file.write("\n")
            file.write(input("Type in contact name, address, phone, and email. (comma seperated)\n"))
        data = pandas.read_csv("contacts.csv")
        contact_dict = data.to_dict(orient="records")
    if choice == "3":
        data.drop([input("Enter the name of the contact you would like to delete: ")], inplace=True)
        data.to_csv('contacts.csv', mode='w')
    if choice == "4":
        data = pandas.read_csv("contacts.csv")
        contact_dict = data.to_dict(orient="records")
        data.set_index("Name", inplace=True)
        print(data.loc[input("Enter the name of the contact you would like to search: \n")])
    if choice == "5":
        print("Goodbye!")
        accessing = False



