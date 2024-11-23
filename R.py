from rotate_face import rotate_face_cw

def perform_r_move(cube):
    """
    Perform the 'R' move (Right face clockwise).
    Modifies the cube by:
    - Rotating the R face clockwise.
    - Adjusting the edges of the neighboring faces (U, F, D, B).
    """
    # Rotate the R face clockwise
    cube["R"] = rotate_face_cw(cube["R"])

    # Adjust the edges of U, F, D, B faces
    right_up = [row[2] for row in cube["U"]]
    right_front = [row[2] for row in cube["F"]]
    right_down = [row[2] for row in cube["D"]]
    right_back = [row[0] for row in reversed(cube["B"])]

    # Shift the edges clockwise
    for i in range(3):
        cube["U"][i][2] = right_front[i]  # Front edge becomes Up edge
        cube["F"][i][2] = right_down[i]  # Down edge becomes Front edge
        cube["D"][i][2] = right_back[i]  # Back edge becomes Down edge
        cube["B"][2 - i][0] = right_up[i]  # Up edge becomes Back edge

