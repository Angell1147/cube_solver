from U import perform_u_move
from D import perform_d_move
from R import perform_r_move
from L import perform_l_move


# Example Usage
rubiks_cube = {
    "U": [  # Up face
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ],
    "F": [  # Front face
        ["R", "R", "R"],
        ["R", "R", "R"],
        ["R", "R", "R"]
    ],
    "R": [  # Right face
        ["B", "B", "B"],
        ["B", "B", "B"],
        ["B", "B", "B"]
    ],
    "B": [  # Back face
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ],
    "L": [  # Left face
        ["G", "G", "G"],
        ["G", "G", "G"],
        ["G", "G", "G"]
    ],
    "D": [  # Down face
        ["Y", "Y", "Y"],
        ["Y", "Y", "Y"],
        ["Y", "Y", "Y"]
    ]
}

# Perform the U move
perform_u_move(rubiks_cube)

# Perform the D move
#erform_d_move(rubiks_cube)

# Perform the R move
#perform_r_move(rubiks_cube)

# Perform the L move
#perform_l_move(rubiks_cube)


# Print the updated cube
for face, matrix in rubiks_cube.items():
    print(f"{face} Face:")
    for row in matrix:
        print(row)
    print()