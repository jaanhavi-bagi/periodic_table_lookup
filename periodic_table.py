import periodic_table_module as ptm

print("Search using atomic number : 1")
print("Search using atom name : 2")
print("Search using atomic symbol : 3")
print("Search a molecule : 4")

a = int(input("Enter how you want to look up element in periodic table : "))

if a == 1:
 ptm.atomic_number()

elif a == 2:
 ptm.element_name()

elif a == 3:
 ptm.atomic_symbol()

elif a ==4:
 ptm.molecule()

else:
 print("Invalid")