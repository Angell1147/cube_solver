from rotate_face import rotate_face_cw

def perform_d_move(cube):
    """
    Perform the 'D' move (Down face clockwise).
    Modifies the cube by:
    - Rotating the D face clockwise.
    - Adjusting the edges of the neighboring faces (F, R, B, L).
    """
    # Rotate the D face clockwise
    cube["D"] = rotate_face_cw(cube["D"])

    # Adjust the edges of F, R, B, L faces
    bottom_front = cube["F"][2][:]
    bottom_right = cube["R"][2][:]
    bottom_back = cube["B"][2][:]
    bottom_left = cube["L"][2][:]

    # Shift the edges clockwise
    cube["F"][2] = bottom_left  # Right edge becomes Front edge
    cube["R"][2] = bottom_front   # Back edge becomes Right edge
    cube["B"][2] = bottom_right   # Left edge becomes Back edge
    cube["L"][2] = bottom_back  # Front edge becomes Left edge


