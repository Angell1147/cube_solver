import tkinter as tk
import backend

def validate_scrambled_state(scrambled_state):
    valid_faces = ['F', 'R', 'B', 'L', 'U', 'D']
    if len(scrambled_state) != 54:
        return False, f"Invalid state length: {len(scrambled_state)}. It must be exactly 54 characters long."
    invalid_characters = [char for char in scrambled_state if char not in valid_faces]
    if invalid_characters:
        return False, f"Invalid characters found: {invalid_characters}. Only 'F', 'R', 'B', 'L', 'U', 'D' are allowed."
    face_counts = {face: scrambled_state.count(face) for face in valid_faces}
    if any(count != 9 for count in face_counts.values()):
        return False, f"Invalid face counts: {face_counts}. Each face must appear exactly 9 times."
    return True, "Valid scrambled state."

GUI_rubiks_cube = {
    "U": [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
    "F": [["B", "B", "B"], ["R", "R", "R"], ["R", "R", "R"]],
    "R": [["O", "O", "O"], ["B", "B", "B"], ["B", "B", "B"]],
    "B": [["G", "G", "G"], ["O", "O", "O"], ["O", "O", "O"]],
    "L": [["R", "R", "R"], ["G", "G", "G"], ["G", "G", "G"]],
    "D": [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]]
}

buttons = []
selected_color = None
solution = None
counter = 0
flag = False

def translate_move(move):
    face_map = {"U": "Up", "F": "Front", "R": "Right", "B": "Back", "L": "Left", "D": "Down"}
    if len(move) == 1:
        return f"{move}: Rotate the {face_map[move]} face by 90 degrees in clockwise direction."
    elif move.endswith("'"):
        return f"{move}: Rotate the {face_map[move[0]]} face by 90 degrees in counterclockwise direction."
    elif move.endswith("2"):
        return f"{move}: Rotate the {face_map[move[0]]} face by 180 degrees in clockwise direction."
    return "Invalid move."

def on_submit(color_key_frame, navigation_frame, message_label, submit_btn):
    global solution, GUI_rubiks_cube, flag
    backend.show(GUI_rubiks_cube)
    if not flag:
        navigation_frame.grid(row=0, column=12, rowspan=9, padx=10)
        scrambled_string = backend.convert_to_kociemba_notation(GUI_rubiks_cube)
        boolen, msg = validate_scrambled_state(scrambled_string)
        message_label.config(text=msg)
        if boolen:
            try:
                temp = backend.kociemba.solve(scrambled_string)
                solution = temp.strip().split()
                for widget in color_key_frame.winfo_children():
                    widget.destroy()
                next_btn = tk.Button(
                    navigation_frame, text="Next", font=("Arial", 12, "bold"),
                    bg="lightblue", width=10, height=2, command=lambda: on_next(message_label)
                )
                next_btn.pack(pady=10)
                prev_btn = tk.Button(
                    navigation_frame, text="Prev", font=("Arial", 12, "bold"),
                    bg="lightblue", width=10, height=2, command=lambda: on_prev(message_label)
                )
                prev_btn.pack(pady=10)
                submit_btn.config(text="Reset")
                flag = True
            except Exception as e:
                message_label.config(text=f"Error solving the cube: {e}")
                flag = False
                navigation_frame.grid_forget(row=0, column=12, rowspan=9, padx=10)
    else:
        reset(color_key_frame, navigation_frame, message_label, submit_btn)

def refresh_gui(buttons):
    global GUI_rubiks_cube
    face_layout = {
        "U": (0, 3), "L": (3, 0), "F": (3, 3),
        "R": (3, 6), "B": (3, 9), "D": (6, 3)
    }
    color_map = {
        "W": "white", "R": "red", "B": "blue",
        "O": "orange", "G": "green", "Y": "yellow"
    }
    indx = 0
    for face, (row_offset, col_offset) in face_layout.items():
        for i in range(3):
            for j in range(3):
                color = color_map[GUI_rubiks_cube[face][i][j]]
                buttons[indx].configure(bg=color)
                indx += 1

def on_next(message_label):
    global counter, solution, GUI_rubiks_cube, buttons
    if solution and counter < len(solution):
        move = solution[counter]
        GUI_rubiks_cube = backend.execute_move(GUI_rubiks_cube, move)
        counter += 1
        refresh_gui(buttons)
        message_label.config(text=translate_move(move))

def on_prev(message_label):
    global counter, solution, GUI_rubiks_cube, buttons
    if solution and counter > 0:
        counter -= 1
        move = solution[counter]
        GUI_rubiks_cube = backend.execute_move(GUI_rubiks_cube, move, reversed=True)
        refresh_gui(buttons)
        message_label.config(text=translate_move(move))

def select_color(color):
    global selected_color
    selected_color = color

def set_box_color(btn, position):
    global GUI_rubiks_cube
    GUI_rubiks_cube[position["face"]][position["indx"][0]][position["indx"][1]] = selected_color[0].upper()
    if selected_color:
        btn.configure(bg=selected_color)

def reset(color_key_frame, navigation_frame, message_label, submit_btn):
    global GUI_rubiks_cube, buttons, selected_color, solution, counter, flag
    GUI_rubiks_cube = {key: [["W"] * 3 for _ in range(3)] for key in GUI_rubiks_cube}
    refresh_gui(buttons)
    
    for widget in navigation_frame.winfo_children():
        widget.destroy()
    
    for widget in color_key_frame.winfo_children():
        widget.destroy()
    navigation_frame.grid_forget()
    # Reinitialize color-picking options
    colors = {
        "white": "U (White)", "red": "F (Red)", "blue": "R (Blue)",
        "orange": "B (Orange)", "green": "L (Green)", "yellow": "D (Yellow)"
    }
    tk.Label(color_key_frame, text="Color Key:", font=("Arial", 12, "bold")).pack(pady=5)
    for color, label in colors.items():
        tk.Button(
            color_key_frame,
            bg=color,
            text=label,
            width=12,
            height=2,
            relief="raised",
            command=lambda c=color: select_color(c)  # Rebind color selection
        ).pack(pady=5)
        

    solution = None
    counter = 0
    flag = False
    selected_color = None
    submit_btn.config(text="Submit")
    message_label.config(text="Reset complete. Redesign the cube.")


def create_cube_gui():
    root = tk.Tk()
    root.title("Rubik's Cube GUI")
    layout = {
        "U": (0, 3), "L": (3, 0), "F": (3, 3),
        "R": (3, 6), "B": (3, 9), "D": (6, 3)
    }
    global buttons
    for face, (row_offset, col_offset) in layout.items():
        for i in range(3):
            for j in range(3):
                position = {"face": face, "indx": [i, j]}
                btn = tk.Button(
                    root, bg="gray", width=4, height=2, relief="flat",
                )
                btn.config(command=lambda b=btn, pos=position: set_box_color(b, pos))
                btn.grid(row=row_offset + i, column=col_offset + j, padx=1, pady=1)
                buttons.append(btn)
    refresh_gui(buttons=buttons)
    color_key_frame = tk.Frame(root)
    color_key_frame.grid(row=0, column=12, rowspan=9, padx=10)

    colors = {
        "white": "U (White)", "red": "F (Red)", "blue": "R (Blue)",
        "orange": "B (Orange)", "green": "L (Green)", "yellow": "D (Yellow)"
    }
    tk.Label(color_key_frame, text="Color Key:", font=("Arial", 12, "bold")).pack(pady=5)
    for color, label in colors.items():
        tk.Button(
            color_key_frame, bg=color, text=label, width=12, height=2, relief="raised",
            command=lambda c=color: select_color(c)
        ).pack(pady=5)

    navigation_frame = tk.Frame(root)
    navigation_frame.grid(row=0, column=12, rowspan=9, padx=10)

    message_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
    message_label.grid(row=10, column=0, columnspan=12)

    submit_btn = tk.Button(
        root, text="Submit", font=("Arial", 12, "bold"), bg="lightblue",
        width=12, height=2, command=lambda: on_submit(color_key_frame, navigation_frame, message_label, submit_btn)
    )
    submit_btn.grid(row=9, column=5, columnspan=3, pady=10)

    root.mainloop()


create_cube_gui()

