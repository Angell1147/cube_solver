import kociemba


def get_cube_input():
    cube = {}
    faces = ["U", "F", "R", "B", "L", "D"]  
    print("Enter the state of the Rubik's Cube:")
    
    for face in faces:
        print(f"Enter the {face} face (3x3 grid), each row of 3 colors separated by spaces:")
        face_matrix = []
        for i in range(3):  # Loop for 3 rows
            inp = input(f"Enter row {i + 1}: ")
            row=[]
            for char in inp:
                row.append(char.upper())
            if len(row) != 3:
                print("Invalid input. Each row must have exactly 3 colors.")
                return None
            face_matrix.append(row)
        cube[face] = face_matrix
    
    return cube

def show(cube):
    for face, matrix in cube.items():
        print(f"{face} Face:")
        for row in matrix:
            print(row)
        print()



def execute_move(cube, move):
    if move == "U":
        return U(cube)
    elif move == "U2":
        return U2(cube)
    elif move == "U'":
        return Up(cube)
    elif move == "R":
        return R(cube)
    elif move == "R2":
        return R2(cube)
    elif move == "R'":
        return Rp(cube)
    elif move == "F":
        return F(cube)
    elif move == "F2":
        return F2(cube)
    elif move == "F'":
        return Fp(cube)
    elif move == "L":
        return L(cube)
    elif move == "L2":
        return L2(cube)
    elif move == "L'":
        return Lp(cube)
    elif move == "D":
        return D(cube)
    elif move == "D2":
        return D2(cube)
    elif move == "D'":
        return Dp(cube)
    elif move == "B":
        return B(cube)
    elif move == "B2":
        return B2(cube)
    elif move == "B'":
        return Bp(cube)
    else:
        print(f"Unknown move: {move}")
        return cube


def convert_to_kociemba_notation(cube):
    order = ["U", "R", "F", "D", "L", "B"]
    face_order = []
    
    for lable in order:
        for face in cube[lable]:
            for row in face:
                for j in row:
                    if j=="W":
                        face_order.append("U")
                    elif j=="R":
                        face_order.append("F")
                    elif j=="B":
                        face_order.append("R")
                    elif j=="G":
                        face_order.append("L")
                    elif j=="O":
                        face_order.append("B")
                    elif j=="Y":
                        face_order.append("D")

    return "".join(face_order)



def U(cube):
    cube["U"] =  [
        [cube["U"][2][0], cube["U"][1][0], cube["U"][0][0]],
        [cube["U"][2][1], cube["U"][1][1], cube["U"][0][1]],
        [cube["U"][2][2], cube["U"][1][2], cube["U"][0][2]],
    ]
    cube["F"][0], cube["R"][0], cube["B"][0], cube["L"][0] = cube["R"][0][:], cube["B"][0][:], cube["L"][0][:], cube["F"][0][:]
    return cube

def U2(cube):
    cube=U(cube)
    cube=U(cube)
    return cube

def Up(cube):
    cube["U"] = [
        [cube["U"][0][2], cube["U"][1][2], cube["U"][2][2]],
        [cube["U"][0][1], cube["U"][1][1], cube["U"][2][1]],
        [cube["U"][0][0], cube["U"][1][0], cube["U"][2][0]],
    ]
    cube["F"][0], cube["R"][0], cube["B"][0], cube["L"][0] = cube["L"][0][:],cube["F"][0][:],cube["R"][0][:],cube["B"][0][:]
    return cube



def R(cube):
    cube["R"]=[
        [cube["R"][2][0], cube["R"][1][0], cube["R"][0][0]],
        [cube["R"][2][1], cube["R"][1][1], cube["R"][0][1]],  
        [cube["R"][2][2], cube["R"][1][2], cube["R"][0][2]]   
    ]
    temp1, temp2 = cube["B"][2][0], cube["D"][2][2]
    for i in range(0, 3):
        cube["F"][i][2], cube["B"][-i-1][0], cube["D"][-i-1][2], cube["U"][i][2] =cube["D"][i][2], cube["U"][i][2], cube["B"][i][0], cube["F"][i][2]
    cube["D"][0][2]=temp1
    cube["F"][2][2]=temp2
    return cube

def R2(cube):
    cube=R(cube)
    cube=R(cube)
    return cube

def Rp(cube):
    cube=R(cube)
    cube=R(cube)
    cube=R(cube)
    return cube



def F(cube):
    cube["F"] = [
        [cube["F"][2][0], cube["F"][1][0], cube["F"][0][0]],  
        [cube["F"][2][1], cube["F"][1][1], cube["F"][0][1]],  
        [cube["F"][2][2], cube["F"][1][2], cube["F"][0][2]]   
    ]
    temp1, temp2=cube["U"][2][2], cube["D"][0][2]
    for i in range(0, 3):
        cube["L"][i][2], cube["R"][i][0], cube["D"][0][-i-1], cube["U"][2][-i-1] =cube["D"][0][i], cube["U"][2][i], cube["R"][i][0], cube["L"][i][2]
    cube["R"][2][0]=temp1
    cube["L"][2][2]=temp2
    return cube

def F2(cube):
    cube=F(cube)
    cube=F(cube)
    return cube

def Fp(cube):
    cube=F(cube)
    cube=F(cube)
    cube=F(cube)
    return cube



def L(cube):
    cube["L"] = [
        [cube["L"][2][0], cube["L"][1][0], cube["L"][0][0]],  
        [cube["L"][2][1], cube["L"][1][1], cube["L"][0][1]],  
        [cube["L"][2][2], cube["L"][1][2], cube["L"][0][2]]   
    ]
    temp1, temp2 = cube["D"][0][0], cube["B"][0][2]
    for i in range(0, 3):
        cube["F"][i][0], cube["B"][i][2], cube["D"][i][0], cube["U"][i][0] = cube["U"][i][0], cube["D"][-i-1][0], cube["F"][i][0], cube["B"][-i-1][2]
    cube["B"][2][2] = temp1
    cube["U"][2][0] = temp2
    return cube

def L2(cube):
    cube = L(cube)
    cube = L(cube)
    return cube

def Lp(cube):
    cube=L(cube)
    cube=L(cube)
    cube=L(cube)
    return cube



def D(cube):
    cube["D"] = [
        [cube["D"][2][0], cube["D"][1][0], cube["D"][0][0]],
        [cube["D"][2][1], cube["D"][1][1], cube["D"][0][1]],
        [cube["D"][2][2], cube["D"][1][2], cube["D"][0][2]],
    ]
    cube["F"][2], cube["R"][2], cube["B"][2], cube["L"][2] = cube["L"][2][:], cube["F"][2][:], cube["R"][2][:], cube["B"][2][:]
    return cube

def D2(cube):
    cube = D(cube)
    cube = D(cube)
    return cube

def Dp(cube):
    cube = D(cube)
    cube = D(cube)
    cube = D(cube)
    return cube



def B(cube):
    cube["B"] = [
        [cube["B"][2][0], cube["B"][1][0], cube["B"][0][0]],
        [cube["B"][2][1], cube["B"][1][1], cube["B"][0][1]],
        [cube["B"][2][2], cube["B"][1][2], cube["B"][0][2]],
    ]
    temp1, temp2 = cube["D"][2][0], cube["U"][0][0]
    for i in range(0, 3):
        cube["L"][i][0], cube["R"][i][2], cube["D"][2][i], cube["U"][0][i] = cube["U"][0][-i-1], cube["D"][2][-i-1], cube["L"][i][0], cube["R"][i][2]
    cube["R"][2][2] = temp1
    cube["L"][2][0] = temp2
    return cube

def B2(cube):
    cube = B(cube)
    cube = B(cube)
    return cube

def Bp(cube):
    cube = B(cube)
    cube = B(cube)
    cube = B(cube)
    return cube







rubiks_cube = {
    "U": [  
        ["R", "R", "B"],
        ["B", "W", "O"],
        ["B", "W", "O"]
    ],
    "F": [  
        ["W", "G", "B"],
        ["R", "R", "W"],
        ["G", "Y", "W"]
    ],
    "R": [  
        ["Y", "Y", "R"],
        ["B", "B", "W"],
        ["R", "R", "R"]
    ],
    "B": [  
        ["Y", "B", "B"],
        ["R", "O", "O"],
        ["Y", "O", "O"]
    ],
    "L": [  
        ["W", "O", "O"],
        ["W", "G", "Y"],
        ["W", "G", "O"]
    ],
    "D": [  
        ["Y", "B", "G"],
        ["Y", "Y", "G"],
        ["G", "G", "G"]
    ]
}

scrambled_cube = convert_to_kociemba_notation(rubiks_cube)
try:
    solution = kociemba.solve(scrambled_cube)
    print("Solution:", solution)
except Exception as e:
    print(f"Error solving the cube: {e}")

print("\n\n\n\n\n\n\n\n\n\n")

for move in solution.strip().split():
    print(f"Executing move: {move}")
    rubiks_cube = execute_move(rubiks_cube, move)
    show(rubiks_cube) 
    print("\n\n\n\n")






rubiks_cube2 = get_cube_input()
if rubiks_cube2:
    show(rubiks_cube2)
    print("\n\n\n\n\n\n")
    scrambled_cube = convert_to_kociemba_notation(rubiks_cube2)
    try:
        solution = kociemba.solve(scrambled_cube)
        print("Solution:", solution)
    except Exception as e:
        print(f"Error solving the cube: {e} 22")

    print("\n\n\n\n\n\n\n\n\n\n")

    for move in solution.strip().split():
        print(f"Executing move: {move}")
        rubiks_cube = execute_move(rubiks_cube2, move)
        show(rubiks_cube2)  
        print("\n\n\n\n")

else:
    print("Invalid cube input. Please try again.")