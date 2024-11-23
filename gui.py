import tkinter as tk
import backend

def validate_scrambled_state(scrambled_state):
    """
    Validates a scrambled Rubik's Cube state.
    :param scrambled_state: A string of 54 characters representing the scrambled cube.
    :return: Tuple (is_valid: bool, message: str).
    """
    # Expected characters for a Rubik's Cube
    valid_faces = ['F', 'R', 'B', 'L', 'U', 'D']

    # 1. Check if the length is 54
    if len(scrambled_state) != 54:
        return False, f"Invalid state length: {len(scrambled_state)}. It must be exactly 54 characters long."

    # 2. Check if only valid characters are used
    invalid_characters = [char for char in scrambled_state if char not in valid_faces]
    if invalid_characters:
        return False, f"Invalid characters found: {invalid_characters}. Only 'F', 'R', 'B', 'L', 'U', 'D' are allowed."

    # 3. Check if each face appears exactly 9 times
    face_counts = {face: scrambled_state.count(face) for face in valid_faces}
    if any(count != 9 for count in face_counts.values()):
        return False, f"Invalid face counts: {face_counts}. Each face must appear exactly 9 times."

    # If all checks pass
    return True, "Valid scrambled state."



# Global variable to store the currently selected color
rubiks_cube = {
    "U": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "F": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "R": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "B": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "L": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "D": [  
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ]
}

selected_color = None
solution = None
counter = 0

def next_handeler():
    global counter
    global solution


def on_submit():
    global solution
    scrambled_string = backend.convert_to_kociemba_notation(rubiks_cube)
    backend.show(rubiks_cube)
    print(scrambled_string)
    boolen, msg = validate_scrambled_state(scrambled_string)
    print(boolen, msg)
    try:
        solution = backend.kociemba.solve(scrambled_string)
        print("Solution:", solution)
        # for move in solution:
        #     print(f"Executing move: {move}")
        #     rubiks_cube = backend.execute_move(rubiks_cube, move)  
        #     print("\n\n\n\n")
    except Exception as e:
        print(f"Error solving the cube: {e} 22")

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
    global rubiks_cube 
    rubiks_cube[position["face"]][position["indx"][0]][position["indx"][1]] = selected_color[0].upper()
    if selected_color:
        btn.configure(bg=selected_color)  # Solid border for better visibility
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
                position = {"face":face,
                            "indx":[i,j]}

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

    submit_btn = tk.Button(
        root,
        text="Submit",
        font=("Arial", 12, "bold"),
        bg="lightblue",
        width=12,
        height=2,
        command=on_submit  # Bind the button to the on_submit function
    )
    
    submit_btn.grid(row=9, column=5, columnspan=3, pady=10)

    # Start the main event loop
    root.mainloop()

# Run the GUI
create_cube_gui()
