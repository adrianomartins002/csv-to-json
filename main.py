import tkinter
import tkinter as tk
from tkinter import filedialog
import csv
import json
import os

# Global variable to store the selected file path
file_path = ""

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

def convert_csv_to_json():
    global file_path
    if file_path == "":
        return

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    json_file_path = os.path.join("docs", os.path.basename(file_path).replace(".csv", ".json"))
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)

    file_path = ""
    tkinter.messagebox.showinfo("Success", "CSV totally converted!")

# Create the tkinter window
window = tk.Tk()
window.title("CSV to JSON Converter")

# Create the select file button
select_button = tk.Button(window, text="Select CSV File", command=select_file)
select_button.pack(pady=20)

# Create the convert button
convert_button = tk.Button(window, text="Convert to JSON", command=convert_csv_to_json)
convert_button.pack(pady=20)

window.mainloop()