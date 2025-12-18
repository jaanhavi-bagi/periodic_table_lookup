import wx
import csv

# ---------- Read CSV ----------
def read_csv():
    with open("periodic_table.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)   # Skip header
        return list(reader)

# ---------- Format Output ----------
def format_output(element):
    return (
        f"Atomic Number: {element[2]}\n"
        f"Name: {element[0]}\n"
        f"Symbol: {element[1]}\n"
        f"Mass: {element[3]}\n"
        f"Density: {element[4]}\n"
        f"Group: {element[5]}\n"
        f"Block: {element[6]}"
    )

# ---------- Search Function ----------
def search(event):
    method = choice.GetSelection()
    query = input_box.GetValue().strip()

    if method == -1 or query == "":
        output_box.SetValue("⚠ Select search type and enter input.")
        return

    data = read_csv()
    result_text = ""

    # --- Search by Atomic Number ---
    if method == 0:
        try:
            num = int(query)
            for element in data:
                if int(element[2]) == num:
                    result_text = format_output(element)
                    break
        except ValueError:
            result_text = "⚠ Invalid atomic number."

    # --- Search by Element Name ---
    elif method == 1:
        query = query.capitalize()
        for element in data:
            if element[0] == query:
                result_text = format_output(element)
                break

    # --- Search by Atomic Symbol ---
    elif method == 2:
        query = query.capitalize()
        for element in data:
            if element[1] == query:
                result_text = format_output(element)
                break

    # --- Search by Molecule (CHEMISTRY-CORRECT) ---
    elif method == 3:
        found = []
        i = 0

        while i < len(query):

            # Ignore numbers and brackets
            if not query[i].isalpha():
                i += 1
                continue

            # 2-letter symbol ONLY if Uppercase + lowercase (Fe, Na, Cl)
            if (i + 1 < len(query) and
                query[i].isupper() and
                query[i + 1].islower()):

                symbol = query[i:i+2]
                matched = False
                for element in data:
                    if element[1] == symbol:
                        found.append(format_output(element))
                        matched = True
                        i += 2
                        break
                if matched:
                    continue

            # Otherwise, take 1-letter symbol (C, N, O, H)
            symbol = query[i].upper()
            for element in data:
                if element[1] == symbol:
                    found.append(format_output(element))
                    break

            i += 1

        if found:
            result_text = "\n-----------------\n".join(found)
        else:
            result_text = "❌ No matching elements found."

    if result_text == "":
        result_text = "❌ No match found."

    output_box.SetValue(result_text)

# ---------------- GUI ----------------

app = wx.App(False)

frame = wx.Frame(None, title="Periodic Table Lookup", size=(500, 420))
panel = wx.Panel(frame)

choice_label = wx.StaticText(panel, label="Select Search Method:")
choice = wx.ComboBox(
    panel,
    choices=[
        "Search by Atomic Number",
        "Search by Element Name",
        "Search by Atomic Symbol",
        "Search by Molecule"
    ],
    style=wx.CB_READONLY
)

input_label = wx.StaticText(panel, label="Enter Value:")
input_box = wx.TextCtrl(panel)

search_button = wx.Button(panel, label="Search")
output_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

# Layout
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(choice_label, 0, wx.ALL, 5)
sizer.Add(choice, 0, wx.EXPAND | wx.ALL, 5)
sizer.Add(input_label, 0, wx.ALL, 5)
sizer.Add(input_box, 0, wx.EXPAND | wx.ALL, 5)
sizer.Add(search_button, 0, wx.ALL | wx.CENTER, 5)
sizer.Add(output_box, 1, wx.EXPAND | wx.ALL, 5)

panel.SetSizer(sizer)

search_button.Bind(wx.EVT_BUTTON, search)

frame.Show()
app.MainLoop()