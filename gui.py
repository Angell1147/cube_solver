import tkinter as tk

# Global variable to store the currently selected color
selected_color = None

def select_color(color):
    """
    Update the global variable with the selected color.
    """
    global selected_color
    selected_color = color
    print(f"Selected color: {selected_color}")

def set_box_color(btn, position):
    """
    Set the color of the clicked box to the currently selected color and print position.
    """
    if selected_color:
        btn.configure(bg="pink")  # Solid border for better visibility
        print(f"Button at {position} set to {selected_color}")  # Print the position and color
    else:
        print("No color selected!")

def create_cube_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Rubik's Cube GUI")

    # Define the initial layout of the cube
    layout = {
        "U": (0, 3),  # Top face at row 0, columns 3-5
        "L": (3, 0),  # Left face at row 3, columns 0-2
        "F": (3, 3),  # Front face at row 3, columns 3-5
        "R": (3, 6),  # Right face at row 3, columns 6-8
        "B": (3, 9),  # Back face at row 3, columns 9-11
        "D": (6, 3)   # Bottom face at row 6, columns 3-5
    }

    # Create the Rubik's Cube grid
    buttons = []
    for face, (row_offset, col_offset) in layout.items():
        for i in range(3):
            for j in range(3):
                # Define the button's position in the grid
                position = f"{face}-{i},{j}"

                # Create the button
                btn = tk.Button(
                    root,
                    bg="gray",  # Default color
                    width=4,
                    height=2,
                    relief="flat"
                )
                btn.grid(
                    row=row_offset + i,
                    column=col_offset + j,
                    padx=1,
                    pady=1
                )

                # Set the command for the button to change color and print its position
                btn.config(command=lambda b=btn, pos=position: set_box_color(b, pos))

                # Append button to the list (for future reference)
                buttons.append(btn)

    # Create a key for selecting colors
    color_key_frame = tk.Frame(root)
    color_key_frame.grid(row=0, column=12, rowspan=9, padx=10)

    # Define the colors and their labels
    colors = {
        "white": "U (White)",
        "red": "F (Red)",
        "blue": "R (Blue)",
        "orange": "B (Orange)",
        "green": "L (Green)",
        "yellow": "D (Yellow)"
    }

    # Label to show the color key
    tk.Label(color_key_frame, text="Color Key:", font=("Arial", 12, "bold")).pack(pady=5)

    # Add the color buttons to the color key
    for color, label in colors.items():
        btn = tk.Button(
            color_key_frame,
            bg=color,
            text=label,
            width=12,
            height=2,
            relief="raised",
            command=lambda c=color: select_color(c)  # Select color for future button clicks
        )
        btn.pack(pady=5)

    # Start the main event loop
    root.mainloop()

# Run the GUI
create_cube_gui()
