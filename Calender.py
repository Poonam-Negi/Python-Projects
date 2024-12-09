# Importing necessary libraries
from tkinter import ttk
import ttkbootstrap as tbs

# Creating the main window using ttkbootstrap theme
root = tbs.Window(themename="cyborg")  # Sets the theme for the window
root.title("Calendar")  # Sets the title of the window
root.geometry("400x400")  # Sets the size of the window

# Function to fetch and display the selected date
def date():
    date = cal.entry.get()  # Gets the date from the calendar entry widget
    date_label.config(text=date)  # Updates the label to show the selected date

# Date entry widget for selecting a date
cal = tbs.DateEntry(root, dateformat="%d/%m/%Y", bootstyle="info")  # Allows date selection with format dd/mm/yyyy
cal.pack(padx=40, pady=40)  # Adds padding around the calendar widget

# Button to show the selected date
btn = ttk.Button(root, text="Show Date", bootstyle="light-outline", command=date)  # Button to trigger the date function
btn.pack(padx=40, pady=45)  # Adds padding around the button

# Label to display the selected date
date_label = ttk.Label(root, text="No Date Selected")  # Default label text
date_label.pack(padx=40, pady=50)  # Adds padding around the label

# Event calling to keep the window open
root.mainloop()  # Starts the Tkinter event loop
