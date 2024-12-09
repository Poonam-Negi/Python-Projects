import tkinter as tk
from tkinter import ttk  

# Main window setup
root = tk.Tk()
root.title("Unit Converter")  # Sets the title of the window
root.geometry("500x400")  # Sets the window size
root.configure(bg="#f0f8ff")  # Light blue background color

# Header section with title
header = tk.Label(root, text="Unit Converter", font=("Helvetica", 20, "bold"), bg="#4682b4", fg="white")
header.pack(fill=tk.X, pady=10)  # The header spans the entire width (X direction) and has padding on top and bottom

# Adding a frame for the input fields and dropdowns
frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)  # Creates a frame with padding inside
frame.pack(pady=20)  # Adds vertical padding around the frame

# Input field for entering the value to be converted
input_label = tk.Label(frame, text="Enter Value:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2f4f4f")
input_label.grid(row=0, column=0, sticky="w", pady=10)  # Label for input field, aligned to the left

input_value = tk.Entry(frame, font=("Helvetica", 14), width=15, relief="solid", borderwidth=1)
input_value.grid(row=0, column=1, pady=10)  # Entry box for the user to input the value

# Dropdown menus for selecting units to convert from and to
units = ["Meters", "Kilometers", "Centimeters", "Millimeters"]  # List of units for conversion

from_label = tk.Label(frame, text="From:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2f4f4f")
from_label.grid(row=1, column=0, sticky="w", pady=10)  # Label for "From" dropdown

from_unit = ttk.Combobox(frame, values=units, font=("Helvetica", 12), state="readonly", width=12)
from_unit.set("Meters")  # Default unit is "Meters"
from_unit.grid(row=1, column=1, pady=10)  # Dropdown for selecting the unit to convert from

to_label = tk.Label(frame, text="To:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2f4f4f")
to_label.grid(row=2, column=0, sticky="w", pady=10)  # Label for "To" dropdown

to_unit = ttk.Combobox(frame, values=units, font=("Helvetica", 12), state="readonly", width=12)
to_unit.set("Kilometers")  # Default unit is "Kilometers"
to_unit.grid(row=2, column=1, pady=10)  # Dropdown for selecting the unit to convert to

# Output label for displaying the converted value
output_label = tk.Label(root, text="Converted Value: ", font=("Helvetica", 14), bg="#f0f8ff", fg="#2e8b57")
output_label.pack(pady=20)  # Label to display the result of the conversion

# Function to perform the conversion
def convert():
    try:
        # Fetch the value from the input field and the selected units from the dropdowns
        value = float(input_value.get())
        from_unit_value = from_unit.get()
        to_unit_value = to_unit.get()

        # Conversion factors for each unit
        conversion_factors = {
            "Meters": 1,
            "Kilometers": 0.001,
            "Centimeters": 100,
            "Millimeters": 1000
        }

        # Perform the conversion
        result = value * (conversion_factors[to_unit_value] / conversion_factors[from_unit_value])
        output_label.config(text=f"Converted Value: {result:.2f}", fg="#2e8b57")  # Display the result
    except ValueError:
        output_label.config(text="Invalid input! Please enter a valid number.", fg="red")  # Handle invalid input

# Button to trigger the conversion
convert_button = tk.Button(
    root, text="Convert", command=convert,
    font=("Helvetica", 14, "bold"), bg="#4682b4", fg="white",
    activebackground="#5f9ea0", activeforeground="white", relief="raised", bd=3, padx=10, pady=5
)
convert_button.pack(pady=10)  # Adds padding around the button

# Footer with credits
footer = tk.Label(root, text="Created with ♥ in Python", font=("Helvetica", 10), bg="#f0f8ff", fg="#696969")
footer.pack(side=tk.BOTTOM, pady=10)  # Footer at the bottom of the window

# Run the main loop to display the window
root.mainloop()
