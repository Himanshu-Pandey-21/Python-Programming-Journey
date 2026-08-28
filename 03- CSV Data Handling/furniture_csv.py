import csv

filename = "furdata.csv"

try:
    file = open(filename, "r")
    file.close()
except FileNotFoundError:
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Furniture ID", "Furniture Name", "Price"])
    file.close()


def add_furniture():
    n = int(input("How many furniture records do you want to add? "))
    file = open(filename, "a", newline="")
    writer = csv.writer(file)

    for i in range(n):
        print(f"\nEnter details for furniture {i + 1}")
        fid = input("Furniture ID: ")
        name = input("Furniture Name: ")
        price = input("Price: ")
        writer.writerow([fid, name, price])

    file.close()
    print("\nRecords added successfully!")


def search_furniture():
    search_id = input("Enter Furniture ID to search: ")
    found = False
    file = open(filename, "r")
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if len(row) > 0 and row[0] == search_id:
            print("\nRecord Found:")
            print("ID:", row[0])
            print("Name:", row[1])
            print("Price:", row[2])
            found = True
            break

    file.close()

    if not found:
        print("Furniture with ID", search_id, "not found.")


while True:
    print("\n---- Furniture Management ----")
    print("1. Add Furniture Records")
    print("2. Search Furniture Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_furniture()
    elif choice == '2':
        search_furniture()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
