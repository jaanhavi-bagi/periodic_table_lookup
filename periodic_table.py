import periodic_table_module as ptm

print("Search using atomic number : 1")
print("Search using atom name     : 2")
print("Search using atomic symbol : 3")
print("Search a molecule          : 4")

try:
    choice = int(input("Enter your choice : "))

    if choice == 1:
        ptm.atomic_number()
    elif choice == 2:
        ptm.element_name()
    elif choice == 3:
        ptm.atomic_symbol()
    elif choice == 4:
        ptm.molecule()
    else:
        print("Invalid choice")

except ValueError:
    print("Please enter a valid number (1-4)")
