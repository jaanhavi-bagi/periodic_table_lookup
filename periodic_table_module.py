def atomic_number():
    try:
        atomic_no = input("Enter the atomic number of element you want to look up : ").strip()
        if not atomic_no:
            print("Atomic number cannot be empty")
            return

        atomic_no = int(atomic_no)

        with open("periodic_table.csv", "r") as csv:
            csv.readline()
            found = False

            for line in csv:
                try:
                    element = line.strip().split(',')
                    if int(element[2]) == atomic_no:
                        found = True
                        print(f"Atomic number : {element[2]}")
                        print(f"Atomic name   : {element[0]}")
                        print(f"Symbol        : {element[1]}")
                        print(f"Mass          : {element[3]}")
                        print(f"Density       : {float(element[4]):.10f}")
                        print(f"Group         : {element[5]}")
                        print(f"Block         : {element[6]}")
                        break
                except (IndexError, ValueError):
                    continue

            if not found:
                print("Element not found")

    except ValueError:
        print("Please enter a valid integer atomic number")
    except FileNotFoundError:
        print("periodic_table.csv file not found")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user")
    except Exception as e:
        print(" Unexpected error:", e)


def element_name():
    try:
        atomic_name = input("Enter element name : ").strip()
        if not atomic_name:
            print("Element name cannot be empty")
            return

        atomic_name = atomic_name.capitalize()

        with open("periodic_table.csv", "r") as csv:
            csv.readline()
            found = False

            for line in csv:
                try:
                    element = line.strip().split(',')
                    if element[0] == atomic_name:
                        found = True
                        print(f"Atomic number : {element[2]}")
                        print(f"Atomic name   : {element[0]}")
                        print(f"Symbol        : {element[1]}")
                        print(f"Mass          : {element[3]}")
                        print(f"Density       : {float(element[4]):.10f}")
                        print(f"Group         : {element[5]}")
                        print(f"Block         : {element[6]}")
                        break
                except (IndexError, ValueError):
                    continue

            if not found:
                print("Element not found")

    except FileNotFoundError:
        print("periodic_table.csv file not found")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user")
    except Exception as e:
        print(" Unexpected error:", e)


def atomic_symbol():
    try:
        atomic_symbol = input("Enter element symbol : ").strip()
        if not atomic_symbol:
            print("Element symbol cannot be empty")
            return

        atomic_symbol = atomic_symbol.capitalize()

        with open("periodic_table.csv", "r") as csv:
            csv.readline()
            found = False

            for line in csv:
                try:
                    element = line.strip().split(',')
                    if element[1] == atomic_symbol:
                        found = True
                        print(f"Atomic number : {element[2]}")
                        print(f"Atomic name   : {element[0]}")
                        print(f"Symbol        : {element[1]}")
                        print(f"Mass          : {element[3]}")
                        print(f"Density       : {float(element[4]):.10f}")
                        print(f"Group         : {element[5]}")
                        print(f"Block         : {element[6]}")
                        break
                except (IndexError, ValueError):
                    continue

            if not found:
                print("Element not found")

    except FileNotFoundError:
        print("periodic_table.csv file not found")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user")
    except Exception as e:
        print("Unexpected error:", e)


def molecule():
    try:
        molecule = input("Enter molecule : ").strip()
        if not molecule:
            print("Molecule cannot be empty")
            return

        if not molecule[0].isupper():
            print("Invalid molecule format")
            return

        elements = set()
        i = 0

        while i < len(molecule):
            if i + 1 < len(molecule) and molecule[i + 1].islower():
                elements.add(molecule[i:i + 2])
                i += 2
            elif molecule[i].isupper():
                elements.add(molecule[i])
                i += 1
            else:
                i += 1

        with open("periodic_table.csv", "r") as csv:
            csv.readline()
            found_any = False

            for line in csv:
                try:
                    element = line.strip().split(',')
                    if element[1] in elements:
                        found_any = True
                        print("\n--------------------------")
                        print(f"Atomic number : {element[2]}")
                        print(f"Atomic name   : {element[0]}")
                        print(f"Symbol        : {element[1]}")
                        print(f"Mass          : {element[3]}")
                        print(f"Density       : {float(element[4]):.10f}")
                        print(f"Group         : {element[5]}")
                        print(f"Block         : {element[6]}")
                except (IndexError, ValueError):
                    continue

            if not found_any:
                print("No valid elements found in molecule")

    except FileNotFoundError:
        print("periodic_table.csv file not found")
    except KeyboardInterrupt:
        print("\n Operation interrupted by user")
    except Exception as e:
        print("Unexpected error:", e)
