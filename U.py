from rotate_face import rotate_face_cw

def perform_u_move(cube):
    """
    Perform the 'U' move (Up face clockwise).
    Modifies the cube by:
    - Rotating the U face clockwise.
    - Adjusting the edges of the neighboring faces (F, R, B, L).
    """
    # Rotate the U face clockwise
    cube["U"] = rotate_face_cw(cube["U"])

    # Adjust the edges of the F, R, B, L faces
    # Save the top edges of F, R, B, L
    top_front = cube["F"][0][:]
    top_right = cube["R"][0][:]
    top_back = cube["B"][0][:]
    top_left = cube["L"][0][:]

    # Shift the edges clockwise
    cube["F"][0] = top_right  # Left edge becomes Front edge
    cube["R"][0] = top_back  # Front edge becomes Right edge
    cube["B"][0] = top_left  # Right edge becomes Back edge
    cube["L"][0] = top_front  # Back edge becomes Left edge

