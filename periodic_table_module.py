def atomic_number():
 atomic_number = int(input("Enter the atomic number of element you want to look up : "))
 read_csv()

 csv = open('periodic_table.csv', 'r')
 csv.readline()
 for line in csv:
  element = line.split(',')
 
  if int(element[2]) == atomic_number: 
   print(f"Atomic number : {element[2]}")
   print(f"Atomic name : {element[0]}")
   print(f"Symbol : {element[1]}")
   print(f"Mass : {element[3]}")
   print(f"Density : {float(element[4]):.10f}")
   print(f"Group : {element[5]}")
   print(f"Block : {element[6]}")


 csv.close()

def element_name():
 atomic_name = input("Enter element name : ")
 atomic_name = atomic_name.capitalize()

 csv = open('periodic_table.csv', 'r')
 csv.readline()

 for line in csv:
  element = line.split(',')
  if element[0] == atomic_name:
   print(f"Atomic number : {element[2]}")
   print(f"Atomic name : {element[0]}")
   print(f"Symbol : {element[1]}")
   print(f"Mass : {element[3]}")
   print(f"Density : {float(element[4]):.10f}")
   print(f"Group : {element[5]}")
   print(f"Block : {element[6]}")

 csv.close()

def atomic_symbol():
 atomic_symbol = input("Enter element symbol : ")
 atomic_symbol = atomic_symbol.capitalize()

 csv = open('periodic_table.csv', 'r')
 csv.readline()

 for line in csv:
  element = line.split(',')
  if element[1] == atomic_symbol:
   print(f"Atomic number : {element[2]}")
   print(f"Atomic name : {element[0]}")
   print(f"Symbol : {element[1]}")
   print(f"Mass : {element[3]}")
   print(f"Density : {float(element[4]):.10f}")
   print(f"Group : {element[5]}")
   print(f"Block : {element[6]}")

 csv.close()

def molecule():
 molecule = input("Enter molecule : ")
 print(molecule)
 
 set1 = set()
 set2 = set()
 set3 = set()
 count = {}

 if molecule.isupper():
  csv = open('periodic_table.csv', 'r')
  csv.readline()
  for line in csv:
   element = line.split(',')
   
   for i in molecule:
    if i == element[1]:
     print(f"Atomic number : {element[2]}")
     print(f"Atomic name : {element[0]}")
     print(f"Symbol : {element[1]}")
     print(f"Mass : {element[3]}")
     print(f"Density : {float(element[4]):.10f}")
     print(f"Group : {element[5]}")
     print(f"Block : {element[6]}")

  csv.close()

  
 else:
  for i in molecule:
   if i.islower():
    n = molecule.find(i)
    element = molecule[n-1:n+1]
    set1.add(element)

   else:
    set1.add(i)

  for i in range(len(molecule)):
   if i + 1 < len(molecule) and molecule[i+1].islower():
    set2.add(molecule[i])

   set3 = set1 - set2

  for i in molecule:
   count.setdefault(i,0)
   count[i] += 1

  for k,v in count.items():
   if v > 1:
    set3.add(k)
 
  csv = open('periodic_table.csv', 'r')
  csv.readline()
  for line in csv:
   element = line.split(',')
   for i in set3:
    if i == element[1]:
     print(f"Atomic number : {element[2]}")
     print(f"Atomic name : {element[0]}")
     print(f"Symbol : {element[1]}")
     print(f"Mass : {element[3]}")
     print(f"Density : {float(element[4]):.10f}")
     print(f"Group : {element[5]}")
     print(f"Block : {element[6]}")
  
  csv.close()





 