from rotate_face import rotate_face_cw

def perform_l_move(cube):
    """
    Perform the 'L' move (Left face clockwise).
    Modifies the cube by:
    - Rotating the L face clockwise.
    - Adjusting the edges of the neighboring faces (U, F, D, B).
    """
    # Rotate the L face clockwise
    cube["L"] = rotate_face_cw(cube["L"])

    # Adjust the edges of U, F, D, B faces
    left_up = [row[0] for row in cube["U"]]
    left_front = [row[0] for row in cube["F"]]
    left_down = [row[0] for row in cube["D"]]
    left_back = [row[2] for row in reversed(cube["B"])]

    # Shift the edges clockwise
    for i in range(3):
        cube["U"][i][0] = left_back[i]   # Back edge becomes Up edge
        cube["F"][i][0] = left_up[i]    # Up edge becomes Front edge
        cube["D"][i][0] = left_front[i] # Front edge becomes Down edge
        cube["B"][2 - i][2] = left_down[i] # Down edge becomes Back edge

