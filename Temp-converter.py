from tkinter import *
from tkinter.font import Font

# Create the main window
window = Tk()
window.title("Temperature Converter")
window.geometry('500x400')
window.config(bg="#002e4d")

# Create a custom font
custom_font = Font(family="Arial", size=13, weight="bold")

# Load the image
pic1 = PhotoImage(file='img\\img1.png')

# Create a label to display the image
label = Label(window, image=pic1)
label.place(x=100,y=40)
label.config(bg="#002e4d")

icon = PhotoImage(file='img\\icon.png')
window.iconphoto(True,icon)


# Create the first dropdown menu
selected_unit = StringVar()
selected_unit.set("Celsius")  # Set the default option
options = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown1 = OptionMenu(window, selected_unit, *options)
dropdown1.config(font=custom_font, width=10 ,relief="raised")
dropdown1.place(x=80, y=140)

transition = Label(window, text=">", font=custom_font,fg="#66ffb3",bg="#002e4d").place(x=241,y=145)

# Create the second dropdown menu
selected_unit2 = StringVar()
selected_unit2.set("Kelvin")  # Set the default option
options2 = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown2 = OptionMenu(window, selected_unit2, *options2 )
dropdown2.config(font=custom_font, width=10 ,relief="raised")
dropdown2.place(x=280, y=140)

# Create the entry box
entry = Entry(window, font=custom_font, width=14 )
entry.place(x=80, y=245)

# Create the label for the converted value
converted_value_label = Label(window, text=" ", font=custom_font,bg="#ffffff",width=13)
converted_value_label.place(x=280, y=245)

# Create the menu bar at the top right
menubar = Menu(window)
window.config(menu=menubar)

# Create the "Group Members" menu
group_menu = Menu(menubar)
menubar.add_cascade(label="Pythonista", menu=group_menu)
group_menu.add_command(label="Tesfaye Zeleke")
group_menu.add_command(label="abizeleke19@gmail.com")
group_menu.config(bg="#ffffff")
# Function to handle the temperature conversion
def convert_temperature(*args):
    try:
        input_value = entry.get()  # Get the input value and remove leading/trailing whitespace
        if input_value:  # Check if the input value is not empty
            input_value = float(input_value)
            from_unit = selected_unit.get()
            to_unit = selected_unit2.get()

            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    converted_value = (input_value * 9/5) + 32
                elif to_unit == "Kelvin":
                    converted_value = input_value + 273.15
                else:
                    converted_value = input_value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    converted_value = (input_value - 32) * 5/9
                elif to_unit == "Kelvin":
                    converted_value = (input_value - 32) * 5/9 + 273.15
                else:
                    converted_value = input_value
            else:  # from_unit == "Kelvin"
                if to_unit == "Celsius":
                    converted_value = input_value - 273.15
                elif to_unit == "Fahrenheit":
                    converted_value = (input_value - 273.15) * 9/5 + 32
                else:
                    converted_value = input_value

            converted_value_label.config(text=f"  {converted_value:.2f}")
        else:
            converted_value_label.config(text="")  # Clear the converted value label when input is empty
    except ValueError:
        converted_value_label.config(text="Invalid input")
# Bind the temperature conversion function to the dropdown menu changes
selected_unit.trace("w", convert_temperature)
selected_unit2.trace("w", convert_temperature)
entry.bind("<KeyRelease>", convert_temperature)

# Start the main event loop
window.mainloop()